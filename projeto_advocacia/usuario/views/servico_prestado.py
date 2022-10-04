from django import forms
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView

from projeto_advocacia.core.forms import CustomModelForm
from projeto_advocacia.core.views import CustomListView, CustomDetailView, CustomCreateView, CustomUpdateView, \
    CustomDeleteView
from projeto_advocacia.processo.models import PrestacaoServico, Lei, ServicoLeis
from projeto_advocacia.usuario.models import Cliente


class PrestacaoServicoForm(forms.ModelForm):
    fields_data_list = None
    class Meta:
        model = PrestacaoServico
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            if self.fields_data_list:
                if visible.name in self.fields_data_list:
                    #visible.field.to_field_name = 'identidade'
                    visible.field.widget = forms.TextInput(attrs=visible.field.widget.attrs)
                    visible.field.widget.attrs['list'] = f"list_{visible.name}"

            if visible.field.__class__.__name__ == "BooleanField":
                visible.field.widget.attrs['class'] = 'form-check-input mb-2'
            else:
                visible.field.widget.attrs['class'] = 'form-control mb-2'


class PrestacaoServicoList(CustomListView):
    class FiltersForm(CustomModelForm):
        class Meta:
            model = PrestacaoServico
            fields = ['responsavel', 'servico', 'descricao', 'valor', 'cliente']

    model = PrestacaoServico
    queryset = PrestacaoServico.objects.all()
    paginate_by = 10
    ordering = ['pk']
    template_name = 'prestacao_servico/list.html'
    raiz = "Prestação de Serviços"
    titulo = "Lista de Prestação de Serviços"
    url_prefix = "prestacao_servicos"
    fields = ['id', 'responsavel', 'servico', 'descricao', 'valor', 'cliente']
    filters_form = FiltersForm


class PrestacaoServicoDetail(CustomDetailView):
    class DetailForm(PrestacaoServicoForm):
        class Meta:
            model = PrestacaoServico
            fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['disabled'] = True

    model = PrestacaoServico
    template_name = 'prestacao_servico/detail.html'
    raiz = "Prestação de Serviços"
    titulo = "Detalhe da Prestação de Serviços"
    url_prefix = "prestacao_servicos"
    form_class = DetailForm

    def get_context_data(self, **kwargs):
        context = super(PrestacaoServicoDetail, self).get_context_data(**kwargs)
        context['lista_leis'] = ServicoLeis.objects.filter(servico=self.object)
        return context


class PrestacaoServicoCreate(TemplateView):
    template_name = 'prestacao_servico/servico.html'
    object_pk = None

    class BuscarClienteForm(PrestacaoServicoForm):
        fields_data_list = ['cliente']
        class Meta:
            model = PrestacaoServico
            fields = ['cliente']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.base_fields['cliente'].required = False

    class ClienteForm(PrestacaoServicoForm):
        class Meta:
            model = Cliente
            fields = '__all__'

    class ServicoForm(PrestacaoServicoForm):
        fields_data_list = ['cliente', 'responsavel', 'processo']
        class Meta:
            model = PrestacaoServico
            fields = '__all__'
            exclude = ['cliente']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.base_fields['responsavel'].to_field_name = 'identidade'
            self.base_fields['processo'].to_field_name = 'numero_processo'

    def get_context_data(self, **kwargs):
        context = super(PrestacaoServicoCreate, self).get_context_data(**kwargs)
        context['buscar_cliente'] = self.BuscarClienteForm()
        context['cliente_form'] = self.ClienteForm()
        context['servico_form'] = self.ServicoForm()
        context['object_list'] = Lei.objects.all()
        return context
        
    def get(self, request, *args, **kwargs):
        return super(PrestacaoServicoCreate, self).get(request, *args, **kwargs)

    def get_form_cliente(self, data):
        return self.ClienteForm(data)

    def get_form_servico(self, data):
        return self.ServicoForm(data)

    def form_valid(self, form):
        return HttpResponseRedirect(reverse('prestacao_servicos_detail', kwargs={'pk': self.object_pk}))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        data = request.POST.dict()
        for index, value in data.items():
            if value == "":
                data[index] = None
        if not data.get('cnh'):
            data["cnh"] = False
        if not data.get('porte'):
            data["porte"] = False
        if data.get('lista_leis'):
            data['lista_leis'] = [int(valor) for valor in str(data['lista_leis']).split(',')]
        print(data)
        if not data.get("cliente"):
            form_cliente = self.get_form_servico(request.POST)
            buscar_cliente = Cliente.objects.filter(identidade=data.get('identidade'))
            if buscar_cliente:
                form_cliente.add_error("identidade", "Já existe um cliente com essa identidade")
            if form_cliente.is_valid():
                cliente = Cliente.objects.create(
                    nome=data.get('nome'),
                    sobrenome=data.get('sobrenome'),
                    identidade=data.get('identidade'),
                    celular=data.get('celular'),
                    idade=data.get('idade'),
                    status=data.get('status'),
                    organizacao=data.get('organizacao'),
                    cnh=data.get('cnh'),
                    porte=data.get('porte')
                )
            else:
                return self.form_invalid(form_cliente)
        print(data)
        form_servico = self.get_form_servico(data)
        if form_servico.is_valid():
            servico = form_servico.save()
            if not servico.cliente:
                servico.cliente = cliente
                servico.save()
            self.object_pk = servico.pk
            for lei_id in data['lista_leis']:
                servico_lei = ServicoLeis.objects.create(
                    servico=servico,
                    leis_id=lei_id
                )
                print(servico_lei)

            return self.form_valid(form_servico)
        else:
            return self.form_invalid(form_servico)

class PrestacaoServicoUpdate(CustomUpdateView):
    class UpdateForm(PrestacaoServicoForm):
        class Meta:
            model = PrestacaoServico
            fields = '__all__'

    model = PrestacaoServico
    template_name = 'prestacao_servico/update.html'
    form_class = UpdateForm
    raiz = "Prestação de Serviços"
    titulo = "Editar Prestação de Serviços"
    url_prefix = "prestacao_servicos"


class PrestacaoServicoDelete(CustomDeleteView):
    class DeleteForm(PrestacaoServicoForm):
        class Meta:
            model = PrestacaoServico
            fields = '__all__'

    model = PrestacaoServico
    template_name = 'prestacao_servico/delete.html'
    raiz = "Prestação de Serviços"
    titulo = "Deletar Prestação de Serviços"
    descricao = "Prestação de Serviços"
    url_prefix = "prestacao_servicos"
    form_class = DeleteForm

