"""Schemas for Persons App."""

from drf_spectacular.utils import extend_schema, OpenApiResponse

from apps.utils.serializers import PictureReadSerializer, PictureWriteSerializer
from apps.mangas.serializers import MangaMinimalSerializer
from apps.characters.serializers import CharacterVoiceReadSerializer
from .serializers import (
    PersonReadSerializer,
    PersonWriteSerializer,
    PersonMinimalSerializer,
)


person_schemas = {
    "list": extend_schema(
        summary="Get Several Persons",
        description="Get a list of available persons.",
        responses={
            200: OpenApiResponse(PersonMinimalSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            404: OpenApiResponse(description="Not Found"),
        },
        auth=[],
        tags=["persons"],
    ),
    "create": extend_schema(
        summary="Create Person",
        description="Create a person, only for `IsContributor` or `IsAdministrator` users.",
        request=PersonWriteSerializer,
        responses={
            201: OpenApiResponse(PersonWriteSerializer, description="Created"),
            400: OpenApiResponse(description="Bad Request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
        tags=["persons"],
    ),
    "retrieve": extend_schema(
        summary="Get Person",
        description="Get detailed information about a specific person.",
        responses={
            200: OpenApiResponse(PersonReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            404: OpenApiResponse(description="Not Found"),
        },
        auth=[],
        tags=["persons"],
    ),
    "update": extend_schema(
        summary="Update Person",
        description="Update all fields of a specific person, only for `IsContributor` or `IsAdministrator` users.",
        request=PersonWriteSerializer,
        responses={
            200: OpenApiResponse(PersonWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["persons"],
    ),
    "partial_update": extend_schema(
        summary="Partial Update Person",
        description="Update some fields of a specific person, only for `IsContributor` or `IsAdministrator` users.",
        request=PersonWriteSerializer,
        responses={
            200: OpenApiResponse(PersonWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["persons"],
    ),
    "destroy": extend_schema(
        summary="Remove Person",
        description="Remove a specific person, only for `IsContributor` or `IsAdministrator` users.",
        responses={
            204: OpenApiResponse(description="No Content"),
            400: OpenApiResponse(description="Bad Request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["persons"],
    ),
    "get_mangas": extend_schema(
        summary="Get Person Mangas",
        description="Get all mangas of an person passed as param (`uuid`).",
        responses={
            200: OpenApiResponse(MangaMinimalSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            404: OpenApiResponse(description="Not Found"),
        },
        auth=[],
        tags=["persons"],
    ),
    "get_pictures": extend_schema(
        summary="Get Person Pictures",
        description="Get all pictures of an person passed as param (`uuid`).",
        responses={
            200: OpenApiResponse(PictureReadSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            404: OpenApiResponse(description="Not Found"),
        },
        auth=[],
        tags=["persons"],
    ),
    "create_picture": extend_schema(
        summary="Create Picture for Person",
        description="Create a picture for a person, only for `IsContributor` or `IsAdministrator` users.",
        request=PictureWriteSerializer,
        responses={
            201: OpenApiResponse(PictureWriteSerializer, description="Created"),
            400: OpenApiResponse(description="Bad Request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
        tags=["persons"],
    ),
    "get_voices": extend_schema(
        summary="Get Person Voices",
        description="Get all voices of an person passed as param (`uuid`).",
        responses={
            200: OpenApiResponse(
                CharacterVoiceReadSerializer(many=True), description="OK"
            ),
            400: OpenApiResponse(description="Bad Request"),
            404: OpenApiResponse(description="Not Found"),
        },
        auth=[],
        tags=["persons"],
    ),
}
