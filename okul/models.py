from django.db import models

class Kadro(models.Model):
  AdiSoyadi = models.CharField(max_length=50)
  Bransi= models.CharField(max_length=11)
  Sinifi = models.CharField(max_length=12 , null='True')
  Aciklama = models.CharField(max_length=250)

  def __str__(self):
        return f"{self.AdiSoyadi} {self.Bransi}"

