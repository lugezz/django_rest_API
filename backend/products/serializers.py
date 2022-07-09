from rest_framework.reverse import reverse
from rest_framework import serializers

from products.models import Product
from products.validators import validate_no_hello_in_title, unique_validator


class ProductSerializer(serializers.ModelSerializer):
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    title = serializers.CharField(validators=[validate_no_hello_in_title, unique_validator])
    # name = serializers.CharField(source='title', read_only=True)

    class Meta:
        model = Product
        fields = [
            'pk',
            'title',
            # 'name',
            'content',
            'price',
            'sale_price',
            'url',
            'edit_url',
        ]

    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f'{value} is already taken, please select a different Product title')
    #     return value

    def get_url(self, obj):
        request = self.context.get("request")

        if not request:
            return None

        return reverse("product-detail", kwargs={'pk': obj.pk}, request=request)

    def get_edit_url(self, obj):
        request = self.context.get("request")

        if not request:
            return None

        return reverse("product-update", kwargs={'pk': obj.pk}, request=request)
