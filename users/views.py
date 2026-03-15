from users.models import User
from users.serializers import UserSerializer
from users.permissions import permissions,IsOwnerorAdmin

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

    permission_classes = [permissions.IsAuthenticated,IsOwnerorAdmin]

    @action(detail=False,methods=["get"])
    def me(self,request):
        # request.user = usuario atual

        serializer = self.get_serializer(request.user) # pega o serializer do usuario atual, transformando os dados do usuario em json
        return Response(serializer.data) # pega os dados do serializer e transforma em json
