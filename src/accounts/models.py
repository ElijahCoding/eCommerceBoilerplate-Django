from django.db import models

class GuestEmail(models.Model):
    email = models.CharField(max_length=120)
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email