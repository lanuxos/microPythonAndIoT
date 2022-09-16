from django.db import models

class TempHumid(models.Model):
    code = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    temperature = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    humidity = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
