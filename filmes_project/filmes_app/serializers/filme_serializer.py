from rest_framework import serializers
from filmes_app.models import Filme, Genero
from .genero_serializer import GeneroSerializer

class FilmeSerializer (serializers.ModelSerializer):
    #o nome genero deve ser igual ao nome especificado no modelo de filme
    #leitura: genero aninhado na resposta
    genero = GeneroSerializer(read_only=True)
    #escrita: recebe apenas o id do genero
    genero_id = serializers.PrimaryKeyRelatedField(
        queryset=Genero.objects.all(), source='genero', write_only=True
    )
    class Meta:
        model = Filme
        fields = '__all__'