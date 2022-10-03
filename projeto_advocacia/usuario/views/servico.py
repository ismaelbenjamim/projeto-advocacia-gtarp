from projeto_advocacia.core.forms import CustomModelForm
from projeto_advocacia.core.views import CustomListView, CustomDetailView, CustomCreateView, CustomUpdateView, \
    CustomDeleteView
from projeto_advocacia.usuario.forms import ServicoForm
from projeto_advocacia.usuario.models import Servico


class ServicoFilters(CustomModelForm):
    class Meta:
        model = Servico
        fields = '__all__'


class ServicoList(CustomListView):
    model = Servico
    queryset = Servico.objects.all()
    paginate_by = 10
    ordering = ['pk']
    template_name = 'servico/list.html'
    raiz = "Serviços"
    titulo = "Lista de Serviços"
    url_prefix = "servicos"
    fields = ['id', 'descricao', 'valor_base', 'cargo_responsavel', 'is_ativo']
    filters_form = ServicoFilters


class ServicoDetail(CustomDetailView):
    model = Servico
    template_name = 'servico/detail.html'
    raiz = "Serviços"
    titulo = "Detalhe do Serviço"
    url_prefix = "servicos"
    fields = ['id', 'descricao', 'valor_base', 'cargo_responsavel', 'is_ativo']


class ServicoCreate(CustomCreateView):
    model = Servico
    template_name = 'servico/create.html'
    form_class = ServicoForm
    raiz = "Serviços"
    titulo = "Adicionar novo Serviço"
    url_prefix = "servicos"


class ServicoUpdate(CustomUpdateView):
    model = Servico
    template_name = 'servico/update.html'
    form_class = ServicoForm
    raiz = "Serviços"
    titulo = "Editar Serviço"
    url_prefix = "servicos"
    campos_filtro = '__all__'


class ServicoDelete(CustomDeleteView):
    model = Servico
    template_name = 'servico/delete.html'
    raiz = "Serviços"
    titulo = "Deletar Serviço"
    descricao = "Serviço"
    url_prefix = "servicos"
    fields = '__all__'
