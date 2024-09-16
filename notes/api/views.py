from rest_framework import mixins, viewsets

from serializers import NoteSerializer


class ListCreateViewSet(mixins.ListModelMix,
                        mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    pass


class NotesViewSet(ListCreateViewSet):
    serializer_class = NoteSerializer
