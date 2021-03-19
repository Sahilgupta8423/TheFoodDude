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

class Orders(models.Model):
    order_id= models.AutoField(primary_key=True)
    items_json= models.CharField(max_length=5000)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    city=models.CharField(max_length=111)
    state=models.CharField(max_length=111)
    zip_code=models.CharField(max_length=111)
    phone=models.CharField(max_length=111)

class Help(models.Model):
    help_id= models.AutoField(primary_key=True)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=111)
    phone=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    city=models.CharField(max_length=111)
    textarea=models.CharField(max_length=1000, default ='')

    def __str__(self):
        return self.name
     
