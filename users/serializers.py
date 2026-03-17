from users.models import User

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = ['first_name','last_name','genero','email','nascimento','cpf',
        'telefone', 'estado', 'cidade','tipo']

class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True) # protege a senha, pra ela so ser lida uma vez

    class Meta():
        model = User
        fields = [
            "email",
            "username",
            "password",
            "genero",
            "nascimento",
            "telefone",
            "cpf",
            "estado",
            "cidade",
            "tipo" 
        ]

        # quando for criar, apaga a senha, e cira usando comando que criptografa e salva
        def create(self, validated_data):

            password = validated_data.pop('password')

            user = User(**validated_data)
            user.set_password(password)
            user.save()

class CustomTokenSerializer(TokenObtainPairSerializer):
    username_field = "email"


        