from pyaspeller import YandexSpeller
from rest_framework import serializers

from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(),
        slug_field="username",
        read_only=True,
    )

    def validate_text(self, value: str) -> str:
        speller = YandexSpeller()
        value = speller.spelled(value)
        return value

    class Meta:
        model = Note
        fields = (
            "id",
            "author",
            "text",
            "pub_date",
        )
