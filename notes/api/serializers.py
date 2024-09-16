from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from models import Note


class NoteSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(),
        slug_field='username',
        read_only=True,
    )

    class Meta:
        model = Note
        fields = ('id', 'author', 'text', 'pub_date',)
