from django.db import models
from django.db.models.query import QuerySet
from django.urls import reverse


class IdManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(
            is_published=Password.Status.PUBLISHED
        )


class Password(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, unique=True, db_index=True)
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(
        choices=Status.choices,
        default=Status.DRAFT
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        null=True
    )

    objects = models.Manager()
    idx = IdManager()

    def __str__(self) -> str:
        return f'Запись: {self.title}'

    def get_absolute_url(self):
        return reverse('pass', kwargs={'pass_slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=128, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True, unique=True)

    def __str__(self) -> str:
        return self.name
