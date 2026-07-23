from denuncias.models import Denuncias

from rest_framework import serializers

class DenunciasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Denuncias
        fields = '__all__'
