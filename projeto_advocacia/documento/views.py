from django.shortcuts import render
from django.urls import reverse_lazy

from projeto_advocacia.core.views import CustomListView, CustomDetailView, CustomCreateView, CustomUpdateView, \
    CustomDeleteView
from projeto_advocacia.documento.forms import DocumentoForm
from projeto_advocacia.documento.models import Documento


class DocumentoList(CustomListView):
    model = Documento
    queryset = Documento.objects.all()
    paginate_by = 10
    ordering = ['pk']
    template_name = 'documento/list.html'
    raiz = "Documentos"
    titulo = "Lista de Documentos"
    fields = ['id', 'descricao', 'responsavel', 'tipo', 'documento_gerado', 'documento_gerado_modelo', 'documento_submetido']

    def campos_tabela(self):
        fields = []
        all_fields = self.model._meta.get_fields()
        if self.fields == '__all__':
            return all_fields
        for field in all_fields:
            if field.name in self.fields:
                fields.append(field)
        return fields

    def get_queryset(self):
        queryset = super(DocumentoList, self).get_queryset()
        if self.request.GET:
            filters = {}
            for index, valor in self.request.GET.items():
                if not valor:
                    continue
                if index == "csrfmiddlewaretoken":
                    continue
                filters[index] = valor
            try:
                queryset = queryset.filter(**filters)
            except:
                return []
        return queryset


class DocumentoDetail(CustomDetailView):
    model = Documento
    template_name = 'documento/detail.html'
    raiz = "Documentos"
    titulo = "Detalhe do Documento"
    campos_tabela = model._meta.get_fields()


class DocumentoCreate(CustomCreateView):
    model = Documento
    template_name = 'documento/create.html'
    form_class = DocumentoForm
    success_url = reverse_lazy("documentos_list")
    raiz = "Documentos"
    titulo = "Adicionar novo documento"


class DocumentoUpdate(CustomUpdateView):
    model = Documento
    template_name = 'documento/update.html'
    form_class = DocumentoForm
    raiz = "Documentos"
    titulo = "Editar Documento"
    campos_filtro = ['autor', 'reu', 'juiz', 'advogado_autor', 'advogado_reu']

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        response = form_class(**self.get_form_kwargs())
        for field in response:
            if field.name in self.campos_filtro:
                field.initial = getattr(self.object, field.name)
        return response


class DocumentoDelete(CustomDeleteView):
    model = Documento
    template_name = 'documento/delete.html'
    success_url = reverse_lazy("documentos_list")
    raiz = "Documentos"
    titulo = "Deletar Documento"
    descricao = "Documento"
    campos_tabela = model._meta.get_fields()
