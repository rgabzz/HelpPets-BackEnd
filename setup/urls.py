from django.contrib import admin
from django.urls import path,include

from rest_framework import routers

from users.views import UserView,RegisterView,LoginView

router = routers.DefaultRouter()
router.register('users', UserView,'usuarios')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view(), name='Registro'),
    path('login/',LoginView.as_view(), name='Login'),
    path('', include(router.urls)),
]
