from django.db import models


class SearchResult(models.Model):
    location = models.CharField(max_length=255)
    checkin = models.DateField()
    checkout = models.DateField()
    guests = models.IntegerField()
    result_data = models.JSONField()

    def __str__(self):
        return f"{self.location} ({self.checkin} - {self.checkout})"
