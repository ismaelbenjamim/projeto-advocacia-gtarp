from django.db.models import Sum
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from projeto_advocacia.processo.apis.serializers import LeiSerializer
from projeto_advocacia.processo.models import Lei


class LeiAPI(viewsets.ModelViewSet):
    queryset = Lei.objects.all()
    serializer_class = LeiSerializer
    http_method_names = ['get', 'post', 'patch']

    class QuerySerializer(serializers.Serializer):
        descricao = serializers.CharField(required=False)
        artigo = serializers.CharField(required=False)

    def get_queryset(self):
        queryset = self.queryset.all()
        descricao = self.request.query_params.get("descricao")
        artigo = self.request.query_params.get("artigo")
        if artigo:
            queryset = queryset.filter(artigo__contains=artigo)
        if descricao:
            queryset = queryset.filter(descricao__contains=descricao)
        return queryset

    @swagger_auto_schema(query_serializer=QuerySerializer())
    def list(self, request, *args, **kwargs):
        return super(LeiAPI, self).list(request, *args, **kwargs)


class AplicacaoPenalAPI(APIView):
    queryset = Lei.objects.all()
    http_method_names = ['get']

    class QuerySerializer(serializers.Serializer):
        leis = serializers.ListSerializer(
            child=serializers.PrimaryKeyRelatedField(queryset=Lei.objects.all()),
            required=True
        )

    class ResponseSerializer(serializers.Serializer):
        meses = serializers.IntegerField(allow_null=True)
        multa = serializers.DecimalField(max_digits=15, decimal_places=2, allow_null=True)
        fianca = serializers.DecimalField(max_digits=15, decimal_places=2, allow_null=True)
        agravante = serializers.ListField(allow_null=True)

    @swagger_auto_schema(query_serializer=QuerySerializer())
    def get(self, request):
        data = request.GET.dict()
        try:
            data['leis'] = [int(value) for value in str(data['leis']).split(",")]
        except:
            response_data = {
                "meses": 0,
                "multa": 0.00,
                "fianca": 0.00,
                "agravante": []
            }
            return Response(response_data, status=status.HTTP_200_OK)
        serializer = self.QuerySerializer(data=data)
        serializer.is_valid(raise_exception=True)

        leis_object_list = Lei.objects.filter(id__in=data['leis'])
        response_data = {
            "meses": leis_object_list.aggregate(Sum('pena_base_meses'))['pena_base_meses__sum'],
            "multa": leis_object_list.aggregate(Sum('pena_base_multa'))['pena_base_multa__sum'],
            "fianca": leis_object_list.aggregate(Sum('pena_fianca'))['pena_fianca__sum'],
            "agravante": [(lei.pena_agravante if lei.pena_agravante != "" else None) for lei in leis_object_list]
        }
        response = self.ResponseSerializer(data=response_data)
        response.is_valid(raise_exception=True)
        return Response(response.data, status=status.HTTP_200_OK)




