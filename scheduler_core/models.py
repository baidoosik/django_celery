from django.db import models


# Create your models here.
class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CrawlingList(TimeStamp):
    description = models.CharField(max_length=500, blank=True)
    url = models.URLField(blank=True)

