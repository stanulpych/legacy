from django.db import models


class Department(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    structure = models.TextField()
    work_at_events = models.TextField()
    internal_events = models.TextField()
    faq = models.TextField()
    useful_sources = models.TextField()

    def __str__(self):
        return self.title








