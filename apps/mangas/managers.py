"""Managers for Mangas App."""

from django.db.models import Q

from apps.utils.managers import BaseManager


class MagazineManager(BaseManager):
    """Manager for Magazine model."""


class MangaManager(BaseManager):
    """Manager for Manga model."""

    def get_popular(self):
        return self.get_available().order_by("-popularity")

    def get_recommendations(self):
        return (
            self.get_available()
            .filter(is_recommended=True)
            .order_by("-updated_at")
            .only(
                "id",
                "name",
                "image",
                "published_from",
                "published_to",
                "media_type",
                "status",
            )
        )

    def get_by_genre(self, genre):
        return (
            self.get_available()
            .filter(genres=genre)
            .only(
                "id",
                "name",
                "image",
                "published_from",
                "published_to",
                "media_type",
                "status",
            )
        )

    def get_similar_mangas(self, manga):
        return (
            self.filter(
                Q(genres__in=manga.genres.all()) | Q(themes__in=manga.themes.all())
            )
            .exclude(id=manga.id)
            .distinct()[:25]
        )
