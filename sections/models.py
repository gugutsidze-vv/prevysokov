from django.conf import settings
from django.db import models
from django.db.models import UniqueConstraint


class Section(models.Model):
    name = models.CharField('Имя', max_length=settings.SECTION_TEXT_LENGTH)
    description = models.TextField('Описание')
    location = models.CharField(
        'Локация', max_length=settings.SECTION_TEXT_LENGTH
    )

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=('name', 'location'),
                name='unique_name_in_location',
                violation_error_message=settings.SECTION_CONSTRAINT_MESSAGE,
            )
        ]

    def __str__(self):
        return self.name
