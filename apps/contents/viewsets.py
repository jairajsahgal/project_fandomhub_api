"""Viewsets for Contents App."""

from django.http import Http404
from django.utils.translation import gettext as _
from rest_framework import viewsets
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.utils.permissions import IsAdminOrReadOnly
from apps.contents.models import (Url, Studio, Genre, Season, Rating, Content)
from apps.contents.serializers import (
    UrlSerializer, StudioSerializer, GenreSerializer, SeasonSerializer,
    RatingSerializer, ContentSerializer
)


class UrlViewSet(viewsets.ModelViewSet):
    """Viewset for managing Url instances."""
    serializer_class = UrlSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return Url.objects.filter(available=True)


class StudioViewSet(viewsets.ModelViewSet):
    """Viewset for managing Studio instances."""
    serializer_class = StudioSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['slug', 'name']

    def get_queryset(self):
        return Studio.objects.filter(available=True)

    @action(detail=True, methods=['get'])
    def content_list(self, request, pk=None):
        """
        Pending.

        Pending.
        """
        try:
            studio = self.get_object()
            contents = Content.objects.filter(studio_id=studio)
            serializer = ContentSerializer(contents, many=True)
            return Response(serializer.data)
        except Http404:
            return Response(
                {'errors': _('Studio not found.')}, status=status.HTTP_404_NOT_FOUND
            )


class GenreViewSet(viewsets.ModelViewSet):
    """
    Viewset for managing Genre instances.

    Pending.
    """
    serializer_class = GenreSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return Genre.objects.filter(available=True)

    def create(self, request, *args, **kwargs):
        """
        Create a new genre.

        Returns
        """
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                {'message': _('Genre created successfully.'), 'data': serializer.data},
                status=status.HTTP_201_CREATED,
                headers=headers
            )
        except Exception as e:
            return Response(
                {'errors': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def destroy(self, request, *args, **kwargs):
        """
        Set 'available' to False for logical deletion of a genre.

        Pending.
        """
        try:
            instance = self.get_object()
            instance.available = False
            instance.save()
            return Response(
                {'message': _('Genre deleted successfully.')}, status=status.HTTP_204_NO_CONTENT
            )
        except Http404:
            return Response(
                {'errors': _('Genre not found.')}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {'errors': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @action(detail=True, methods=['get'])
    def content_list(self, request, pk=None):
        """
        Lists anime contents associated with a specific genre.

        Pending.
        """
        try:
            genre = self.get_object()
            contents = Content.objects.filter(genre_id=genre)
            serializer = ContentSerializer(contents, many=True)
            return Response(serializer.data)
        except Http404:
            return Response(
                {'errors': _('Genre not found.')}, status=status.HTTP_404_NOT_FOUND
            )


class SeasonViewSet(viewsets.ModelViewSet):
    """Viewset for managing Season instances."""
    serializer_class = SeasonSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return Season.objects.filter(available=True)


class RatingViewSet(viewsets.ModelViewSet):
    """Viewset for managing Rating instances."""
    serializer_class = RatingSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return Rating.objects.filter(available=True)


class ContentViewSet(viewsets.ModelViewSet):
    """Viewset for managing Content instances."""
    serializer_class = ContentSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['name',]

    def get_queryset(self):
        return Content.objects.filter(available=True)
