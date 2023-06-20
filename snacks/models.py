from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.
class Snack(models.Model):
    name = models.CharField(max_length=64)
    desc = models.TextField()
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('snack_detail', args=[self.id])