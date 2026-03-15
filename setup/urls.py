from django.contrib import admin
from django.urls import path,include

from rest_framework import routers

from users.views import UserViewset

router = routers.DefaultRouter()
router.register('users', UserViewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
