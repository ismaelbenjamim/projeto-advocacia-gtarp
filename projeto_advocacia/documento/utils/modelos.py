from rest_framework import serializers


class HonorariosSerializer(serializers.Serializer):
    nome = serializers.CharField()
    sobrenome = serializers.CharField(required=False)


TIPOS_MODELO_DUCUMENTO = (
    ('honorarios', 'Honorários'),
)


class DocumentoModelo:
    honorarios = HonorariosSerializer

    @staticmethod
    def get_modelo(modelo_str):
        if hasattr(DocumentoModelo, modelo_str):
            return getattr(DocumentoModelo, modelo_str)
        else:
            return None
