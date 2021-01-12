from django.db import models

from users.models import User


class Car(models.Model):
    name_ru = models.CharField(max_length=24)
    name_en = models.CharField(max_length=24)
    released_at = models.DateTimeField()
    added_at = models.DateTimeField(auto_now_add=True, db_index=True)
    owner = models.ForeignKey(User, default=None, on_delete=models.CASCADE, related_name="personal_cars")


    def __str__(self):
        return f"{self.name_ru} | {self.name_en}"

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"