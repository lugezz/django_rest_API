from rest_framework import generics

from articles.models import Article
from articles.serializers import ArticleSerializer


class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.public()
    serializer_class = ArticleSerializer


class ArticleDetailView(generics.RetrieveAPIView):
    queryset = Article.objects.public()
    serializer_class = ArticleSerializer
