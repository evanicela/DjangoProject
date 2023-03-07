from django.db import models


# Create your models here.
class Shoe(models.Model):
    shoe_name = models.CharField(max_length=100)
    shoe_image = models.ImageField(null=True, blank=True, upload_to="images/")
    shoe_price = models.CharField(max_length=100)
    shoe_description = models.CharField(max_length=15)

    class Meta:
        db_table = "shoe"