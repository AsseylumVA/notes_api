from rest_framework import generics, viewsets

from .serializers import NoteSerializer


class NoteViewSet(generics.ListCreateAPIView,
                  viewsets.GenericViewSet):
    serializer_class = NoteSerializer

    def get_queryset(self):
        return self.request.user.notes.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
