import django_filters
from .models import Denuncias

class DenunciasFilter(django_filters.FilterSet):
    class Meta:
        model = Denuncias
        fields = [
            'cidade',
            'usuario_id',
            'status',
        ]
