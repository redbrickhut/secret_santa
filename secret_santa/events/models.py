from datetime import datetime

import pytz
from django.core.validators import MinValueValidator, \
    MaxValueValidator
from django.db import models

# Create your models here.
from users.models import CustomUser


class Event(models.Model):
    class EventStatus(models.TextChoices):
        INACTIVE = 'I'
        ACTIVE = 'A'
        CONCLUDED = 'C'

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='event_pictures', null=True, blank=True)
    game_length = models.IntegerField(
        validators=(MinValueValidator(3), MaxValueValidator(60)))
    created_at = models.DateTimeField(auto_now_add=True)
    activated_at = models.DateTimeField(null=True, blank=True)
    concluded_at = models.DateTimeField(null=True, blank=True)

    revealed = models.BooleanField(default=True)
    owner = models.ForeignKey(CustomUser, related_name='owned_events', on_delete=models.CASCADE)
    participants = models.ManyToManyField(CustomUser, related_name='events')

    @property
    def status(self):

        if not self.activated_at:
            return Event.EventStatus.INACTIVE
        elif datetime.now(pytz.utc) < self.concluded_at:
            return Event.EventStatus.ACTIVE
        else:
            return Event.EventStatus.CONCLUDED

    def __str__(self):
        return f"<Event: {self.name}>"


class Emoji(models.Model):
    image = models.ImageField(upload_to='emojis', null=False, blank=False)
    name = models.CharField(max_length=20, blank=False, null=False)
    description = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return f"<Emoji: {self.name}>"


class Gift(models.Model):
    message = models.CharField(max_length=100, blank=True, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE,
                              related_name='gifts',
                              related_query_name='gifts')

    donor = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING,
                              related_name='+')
    recipient = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING,
                                  related_name='+')
    emoji = models.ForeignKey(Emoji, on_delete=models.DO_NOTHING, null=True)

    opened = models.BooleanField(default=False)
