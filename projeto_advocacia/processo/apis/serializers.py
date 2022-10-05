from rest_framework import serializers

from projeto_advocacia.processo.models import Processo, Lei
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


class LeiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lei
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['categoria'] = instance.get_categoria_display()
        return representation
