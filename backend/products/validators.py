from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from products.models import Product


# def validate_title(value):
#     qs = Product.objects.filter(title__iexact=value)
#     if qs.exists():
#         raise serializers.ValidationError(f'{value} is already taken, please select a different Product title')
#     return value

def validate_no_hello_in_title(value):
    if 'hello' in value.lower():
        raise serializers.ValidationError(f'{value} is not a valid title')


unique_validator = UniqueValidator(Product.objects.all(), lookup='iexact')
