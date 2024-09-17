from rest_framework import mixins, viewsets

from .serializers import NoteSerializer


class ListCreateViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    pass


class NoteViewSet(ListCreateViewSet):
    serializer_class = NoteSerializer

    def get_queryset(self):
        return self.request.user.notes.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
