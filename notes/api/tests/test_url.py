from django.contrib.auth import get_user_model
from django.test import TestCase, Client, override_settings

from ..models import Note

User = get_user_model()
Path = "/api/v1/notes/"


class UrlTests(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        cls.user = User.objects.create_user("testuser")
        cls.user2 = User.objects.create_user("testuser2")
        users = [cls.user, cls.user2]
        for user in users:
            for i in range(5):
                Note.objects.create(
                    author=user,
                    text="test text {i}",
                )

    def setUp(self) -> None:
        self.guest_client = Client()
        self.client = Client()
        self.client.force_login(self.user)

    def test_notes_get_unauthorized(self):
        response = self.guest_client.get(Path)
        self.assertEqual(response.status_code, 403)

    def test_create_authorized(self):
        response = self.client.post(
            Path,
            {"text": "test text"},
        )
        self.assertEqual(response.status_code, 201)

    def test_authorized_only_owner_notes(self):
        response = self.client.get(Path)
        self.assertEqual(response.status_code, 200)

        response_json = response.json()
        for n in response_json.get("results"):
            self.assertEqual(n["author"], self.user.username)

    def test_YandexSpeller(self):
        response = self.client.post(Path, {"text": "СлоМайНый Текуст"})
        self.assertEqual(response.status_code, 201)

        response_json = response.json()
        self.assertEqual(response_json.get("text"), "Сломанный Текст")
