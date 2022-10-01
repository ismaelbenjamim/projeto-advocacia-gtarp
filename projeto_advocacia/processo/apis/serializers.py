from rest_framework import serializers

from projeto_advocacia.processo.models import Processo
from projeto_advocacia.usuario.models import Cliente


class ProcessoSerializer(serializers.ModelSerializer):
    autor = serializers.StringRelatedField()
    reu = serializers.StringRelatedField()
    juiz = serializers.StringRelatedField()
    advogado_autor = serializers.StringRelatedField()
    advogado_reu = serializers.StringRelatedField()
    class Meta:
        model = Processo
        fields = '__all__'
