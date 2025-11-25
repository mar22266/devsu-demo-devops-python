from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.dni}"
