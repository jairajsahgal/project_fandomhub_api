"""ViewSets for Persons App."""

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.utils.translation import gettext as _
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema_view, extend_schema

from apps.utils.mixins import LogicalDeleteMixin
from apps.utils.permissions import IsStaffOrReadOnly
from apps.utils.pagination import MediumSetPagination
from apps.contents.models import Manga
from apps.contents.serializers import MangaListSerializer
from .models import Author
from .serializers import AuthorSerializer
from .schemas import author_schemas


@extend_schema_view(**author_schemas)
class AuthorViewSet(LogicalDeleteMixin, ModelViewSet):
    """
    ViewSet for managing Author instances.

    Endpoints:
    - GET /api/v1/authors/
    - POST /api/v1/authors/
    - GET /api/v1/authors/{id}/
    - PUT /api/v1/authors/{id}/
    - PATCH /api/v1/authors/{id}/
    - DELETE /api/v1/authors/{id}/
    """

    serializer_class = AuthorSerializer
    permission_classes = [IsStaffOrReadOnly]
    search_fields = ["name"]
    ordering_fields = ["name"]
    ordering = ["id"]

    def get_queryset(self):
        return Author.objects.get_available().only("id", "name")

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Get Mangas for Author",
        description="Retrieve a list of mangas for author.",
    )
    @action(detail=True, methods=["get"], url_path="mangas")
    @method_decorator(cache_page(60 * 60 * 2))
    def manga_list(self, request, pk=None):
        """
        Retrieve a list of mangas for the specified author.
        """
        manga_list = Manga.objects.filter(author=pk)
        if manga_list.exists():
            paginator = MediumSetPagination()
            paginated_data = paginator.paginate_queryset(manga_list, request)
            serializer = MangaListSerializer(paginated_data, many=True)
            return paginator.get_paginated_response(serializer.data)
        return Response(
            {"detail": _("There are no mangas for this author.")},
            status=status.HTTP_404_NOT_FOUND,
        )
