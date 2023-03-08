from django.db import models
from .validators import validate_no_special_characters
# Create your models here.

class Goods(models.Model):
    title = models.CharField(max_length=30)
    PRICE_CHOICES = [
        (1, "5000원"),
        (2, "4000원"),
        (3, "3000원"),
        (4, "2000원"),
        (5, "1000원"),
    ]
    price = models.IntegerField(choices=PRICE_CHOICES, default=None)

    image1 = models.ImageField(upload_to="review_pics")
    image2 = models.ImageField(upload_to="review_pics", blank=True)
    image3 = models.ImageField(upload_to="review_pics", blank=True)
    content = models.TextField()
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title