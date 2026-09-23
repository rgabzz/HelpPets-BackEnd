from denuncias.models import Denuncias

from rest_framework import serializers

class DenunciasSerializer(serializers.ModelSerializer):
    condicao = serializers.ListField(
        child=serializers.ChoiceField(
            choices=[choice[0] for choice in Denuncias.CONDICAO_CHOICES]
        )
    )

    class Meta:
        model = Denuncias
        fields = '__all__'
        read_only_fields = ['usuario']