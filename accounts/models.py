from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


one_word_validator = RegexValidator(
    regex=r'^\S+$',
    message="Display name must be a single word (no spaces)."
)


class Account(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="accounts"
    )

    profile_pic = models.ImageField(
        upload_to="Account/",
        blank=True,
        null=True
    )

    dob = models.DateField("Date of Birth")

    display_name = models.CharField(
        max_length=8,
        validators=[one_word_validator],
        unique=True
    )

    def __str__(self):
        return self.display_name
