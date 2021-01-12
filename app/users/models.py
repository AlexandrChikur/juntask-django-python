from django.db import models
from django import forms


class User(models.Model):
    LANGUAGE_CHOICES = [
        ("ru", "ru"), 
        ("en", "en")
    ]

    name = models.CharField("Name", max_length=18, db_index=True)
    email = models.EmailField("E-mail")
    lang = models.CharField("Language", max_length=2, choices=LANGUAGE_CHOICES, default="ru")


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"