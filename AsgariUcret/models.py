from django.db import models


# Create your models here.

class AsgariUcret(models.Model):
    Id = models.AutoField(primary_key=True)
    donem = models.CharField(max_length=6)
    gunluk_altsinir = models.FloatField()
    gunluk_ustsinir = models.FloatField()
    aylik_altsinir = models.FloatField()
    aylik_ustsinir = models.FloatField()
