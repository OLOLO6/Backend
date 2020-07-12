from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from users.permissions import IsClient, IsConsultant
from .serializers import *
from .models import *
from rest_framework.permissions import AllowAny
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import PermissionDenied, NotFound
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404


class VoteViewSet(ModelViewSet):
    # permission_classes = [IsClient | IsConsultant | IsAdminUser]
    permission_classes = [AllowAny]
    serializer_class = VoteSerializer

    def get_queryset(self):
        queryset = Vote.objects.filter(article_id=self.kwargs["pk"])
        return queryset

    def perform_create(self, serializer):
        article = Article.objects.get(id=self.kwargs['pk'], status=True)
        return serializer.save(user=self.request.user, article=article)


class ArticleViewSet(ModelViewSet):
    # permission_classes = [IsConsultant | IsAdminUser]
    permission_classes = [AllowAny]
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    pagination_class = PageNumberPagination

    def get_queryset(self):
        queryset = Article.objects.filter(status=True)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
