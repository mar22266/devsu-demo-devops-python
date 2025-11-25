from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import User


class UserApiTests(APITestCase):
    def setUp(self) -> None:
        self.list_url = reverse("users-list")

    def test_create_user(self):
        payload = {
            "name": "Andre",
            "dni": "123456789",
        }

        response = self.client.post(self.list_url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().dni, "123456789")

    def test_prevent_duplicate_dni(self):
        User.objects.create(name="Existing", dni="123456789")

        payload = {
            "name": "Duplicate",
            "dni": "123456789",
        }

        response = self.client.post(self.list_url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)

    def test_list_users(self):
        User.objects.create(name="User One", dni="111111111")
        User.objects.create(name="User Two", dni="222222222")

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_healthcheck_endpoint(self):
        response = self.client.get("/health/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["status"], "ok")
