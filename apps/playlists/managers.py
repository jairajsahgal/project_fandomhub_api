"""Managers for Playlists App."""

from django.db.models import Manager


class PlaylistManager(Manager):
    """Manager for Author model."""

    def get_available(self):
        return self.filter(available=True)
