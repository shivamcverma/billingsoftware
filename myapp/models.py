from django.db import models

# Create your models here.
class adminlogintbl(models.Model):
    id=models.AutoField(primary_key=True)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.email}, {self.password}"

from django.db import models

class additemstbl(models.Model):
    id = models.AutoField(primary_key=True)
    ItemName = models.CharField(max_length=100)
    Itemquantity = models.CharField(null=True, blank=True)
    Itemprice = models.CharField(max_length=100, null=True, blank=True)
    Ifile = models.ImageField(null=True, blank=True, default="")

    def __str__(self):
        return f"{self.ItemName}, {self.Itemquantity}, {self.Itemprice}, {self.Ifile}"

class customertbl(models.Model):
    id=models.AutoField(primary_key=True)
    customername=models.CharField(max_length=100)
    customermobile=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.id}, {self.customername}, {self.customermobile}"