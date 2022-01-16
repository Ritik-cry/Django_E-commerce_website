from django.db import models

# Create your models here.
class Product(models.Model):
    productName = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    price = models.IntegerField()
    desc = models.CharField(max_length=50)
    image = models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.productName

class Contact(models.Model):
    name = models.CharField(max_length=30,default='')
    email = models.CharField(max_length=30,default='')
    phone = models.IntegerField(default='')
    text = models.CharField(max_length=100,default='')

    def __str__(self):
        return self.name

class Orders(models.Model):
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=30,default='')
    email = models.CharField(max_length=30,default='')
    address = models.CharField(max_length=300,default='')
    phone = models.IntegerField(default='')
    city = models.CharField(max_length=100,default='')
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Tracker(models.Model):
    orderId = models.IntegerField(default="")
    trackerDesc = models.CharField(max_length=1000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.trackerDesc[0:10] + ".."