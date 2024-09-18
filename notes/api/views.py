from django.db.models import QuerySet
from rest_framework import generics, viewsets

from .serializers import NoteSerializer


class NoteViewSet(generics.ListCreateAPIView, viewsets.GenericViewSet):
    serializer_class = NoteSerializer

    def get_queryset(self) -> QuerySet:
        return self.request.user.notes.all()

    def perform_create(self, serializer: NoteSerializer):
        serializer.save(author=self.request.user)
