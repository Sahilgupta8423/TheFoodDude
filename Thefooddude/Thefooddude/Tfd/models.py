from django.db import models

# Create your models here.

class Restaurant(models.Model):
    res_id = models.AutoField(primary_key=True)
    res_title = models.CharField(max_length=100)
    res_spec = models.CharField(max_length=70, default="")
    res_image = models.ImageField(upload_to='Tfd/images', default="")
    address = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.res_title


class Food(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    food_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='Tfd/images', default="")
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name
