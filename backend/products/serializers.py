from rest_framework.reverse import reverse
from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'url',
            'edit_url',
        ]

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
