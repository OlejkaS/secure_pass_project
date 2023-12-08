from django.db import models


class Password(models.Model):
    title = models.CharField(max_length=128)
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Название записи: {self.title}, id записи: {self.pk}'
