from users.models import User
from users.serializers import UserSerializer,RegisterSerializer,CustomTokenSerializer
from users.permissions import permissions,IsOwnerorAdmin

from rest_framework import viewsets,generics
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

    permission_classes = [permissions.IsAuthenticated,IsOwnerorAdmin]

    @action(detail=False,methods=["get","patch"])
    def me(self,request):
        # request.user = usuario atual

        if request.method == "GET":
            serializer = self.get_serializer(request.user) # pega o serializer do usuario atual, transformando os dados do usuario em json
            return Response(serializer.data) # pega os dados do serializer e transforma em json
        
        if request.method == "PATCH":
            serializer = self.get_serializer(
                request.user,
                request.data,
                partial=True
                )
            
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data)
  
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class LoginView(TokenObtainPairView):
    serializer_class =  CustomTokenSerializer