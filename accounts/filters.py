import django_filters
from django_filters import CharFilter

from .models import *

class UserFilter(django_filters.FilterSet):
    first_name = CharFilter(field_name="first_name", lookup_expr='icontains')
    last_name = CharFilter(field_name="last_name", lookup_expr='icontains')
    email = CharFilter(field_name="email", lookup_expr='icontains')
    passout_year = CharFilter(field_name="passout_year", lookup_expr='icontains')
    company = CharFilter(field_name="company", lookup_expr='icontains')
    