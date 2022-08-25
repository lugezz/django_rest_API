from rest_framework import serializers

from api.serializers import UserPublicSerializer
from articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    author = UserPublicSerializer(source='user', read_only=True)

    class Meta:
        model = Article
        fields = [
            'pk',
            'author',
            'title',
            'body',
            'path',
            'endpoint',
        ]
