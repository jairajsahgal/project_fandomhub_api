"""ViewSets for Characters App."""

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext as _
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema_view

from apps.utils.mixins import ListCacheMixin, LogicalDeleteMixin
from apps.utils.models import Picture
from apps.utils.serializers import PictureReadSerializer, PictureWriteSerializer
from apps.animes.serializers import AnimeMinimalSerializer
from apps.mangas.serializers import MangaMinimalSerializer
from apps.characters.models import CharacterVoice
from apps.persons.models import Person
from apps.persons.serializers import PersonMinimalSerializer
from apps.users.permissions import IsContributor
from .models import Character, CharacterAnime, CharacterManga
from .serializers import CharacterReadSerializer, CharacterWriteSerializer
from .filters import CharacterFilter
from .schemas import character_schemas


@extend_schema_view(**character_schemas)
class CharacterViewSet(ListCacheMixin, LogicalDeleteMixin, ModelViewSet):
    """
    ViewSet for managing Characters instances.

    Endpoints:
    - GET /api/v1/characters/
    - POST /api/v1/characters/
    - GET /api/v1/characters/{id}/
    - PUT /api/v1/characters/{id}/
    - PATCH /api/v1/characters/{id}/
    - DELETE /api/v1/characters/{id}/
    """

    permission_classes = [IsContributor]
    serializer_class = CharacterWriteSerializer
    search_fields = ["name", "name_kanji"]
    filterset_class = CharacterFilter

    def get_queryset(self):
        return Character.objects.get_available()

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return CharacterReadSerializer
        return super().get_serializer_class()

    @action(
        detail=True,
        methods=["get", "post"],
        permission_classes=[AllowAny],
        url_path="pictures",
    )
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent", "Accept-Language"))
    def get_pictures(self, request, pk=None, *args, **kwargs):
        """
        Action get all pictures for a character.

        Endpoints:
        - GET api/v1/characters/{id}/pictures/
        """
        character = self.get_object()
        pictures = Picture.objects.get_character_pictures(character)

        if pictures:
            serializer = PictureReadSerializer(pictures, many=True)
            return Response(serializer.data)

        return Response(
            {"detail": _("There is no pictures associated with this character.")},
            status=status.HTTP_404_NOT_FOUND,
        )

    @action(
        detail=True,
        methods=["get", "post"],
        permission_classes=[IsContributor],
        url_path="pictures/create",
    )
    def create_picture(self, request, pk=None, *args, **kwargs):
        """
        Action create picture for a character.

        Endpoints:
        - POST api/v1/characters/{id}/pictures/create/
        """
        serializer = PictureWriteSerializer(data=request.data)
        if serializer.is_valid():
            character = self.get_object()
            character_model = ContentType.objects.get_for_model(Character)
            serializer.save(
                content_type=character_model,
                object_id=character.pk,
            )
            return Response(
                {"detail": _("Picture uploaded successfully.")},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(
        detail=True,
        methods=["get"],
        permission_classes=[AllowAny],
        url_path="voices",
    )
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent", "Accept-Language"))
    def get_voices(self, request, *args, **kwargs):
        """
        Action retrieve voices associated with a character.

        Endpoints:
        - GET api/v1/characters/{id}/voices/
        """
        character = self.get_object()

        try:
            character_anime = CharacterVoice.objects.filter(character_id=character)
            voice_ids = character_anime.values_list("voice_id", flat=True)
            persons = Person.objects.filter(id__in=voice_ids)
            serializer = PersonMinimalSerializer(persons, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @action(
        detail=True,
        methods=["get"],
        permission_classes=[AllowAny],
        url_path="anime",
    )
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent", "Accept-Language"))
    def get_anime(self, request, *args, **kwargs):
        """
        Action retrieve the anime associated with a character.

        Endpoints:
        - GET api/v1/characters/{id}/anime/
        """
        character = self.get_object()
        character_anime = CharacterAnime.objects.filter(
            character_id=character
        ).first()  # TODO: Add manager
        if character_anime:
            anime = character_anime.anime_id
            serializer = AnimeMinimalSerializer(anime)
            return Response(serializer.data)
        return Response(
            {"detail": _("No anime found for this character.")},
            status=status.HTTP_404_NOT_FOUND,
        )

    @action(
        detail=True,
        methods=["get"],
        permission_classes=[AllowAny],
        url_path="manga",
    )
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent", "Accept-Language"))
    def get_manga(self, request, *args, **kwargs):
        """
        Action retrieve the manga associated with a character.

        Endpoints:
        - GET api/v1/characters/{id}/manga/
        """
        character = self.get_object()
        character_manga = CharacterManga.objects.filter(
            character_id=character
        ).first()  # TODO: Add manager
        if character_manga:
            manga = character_manga.manga_id
            serializer = MangaMinimalSerializer(manga)
            return Response(serializer.data)
        return Response(
            {"detail": _("No manga found for this character.")},
            status=status.HTTP_404_NOT_FOUND,
        )
