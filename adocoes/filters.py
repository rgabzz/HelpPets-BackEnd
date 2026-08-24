import django_filters
from .models import Animal

class AnimalFilters(django_filters.FilterSet):

    cidade =django_filters.CharFilter(
        field_name= 'ong__usuario__cidade',
        lookup_expr='iexact'
    )

    class Meta:
        model = Animal
        fields = [
            'especie',
            'raca',
            'ong',
            'status_adocao',
        ]