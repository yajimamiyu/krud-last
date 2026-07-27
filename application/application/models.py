from django.db import models
from django.contrib.auth.models import User


class Application(models.Model):

    TYPE_CHOICES = [
        ('paid', '有給申請'),
        ('overtime', '残業申請'),
        ('expense', '経費申請'),
    ]

    STATUS_CHOICES = [
        ('pending', '承認待ち'),
        ('approved', '承認済み'),
        ('rejected', '却下'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    application_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES
    )

    title = models.CharField(
        max_length=100
    )

    content = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title