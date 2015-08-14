from django.db import models
from model_utils.models import TimeStampedModel

class Info(TimeStampedModel):
    class Meta:
        ordering = ('-created', 'priority', )

    priority = models.IntegerField(
            help_text='Priority from 1 to 10, 10 being highest',
            default=1)

    subject = models.CharField(
            max_length=1024,
            help_text='A hinting subject')

    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return "[{}] {}".format(self.id, self.subject)

    def save(self, *args, **kwargs):
        if self.priority > 10:
            self.priority = 3
        return super().save(*args, **kwargs)

class PhoneNumber(TimeStampedModel):
    class Meta:
        ordering = ('number',)

    name = models.CharField(help_text="A fitting name", max_length=255)
    number = models.CharField(help_text="The phone number", max_length=255)
    comment = models.TextField(blank=True, null=True)


    def __str__(self):
        return "[{}] {}".format(self.number, self.name)

class LinkList(TimeStampedModel):
    
    name = models.CharField(help_text="A fitting name", max_length=255)
    url = models.URLField()

