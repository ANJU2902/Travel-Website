from django.db import models
class traveldb(models.Model):
    name=models.CharField(max_length=100,null=True,blank=False)
    location=models.CharField(max_length=100,null=True,blank=False)
    photo=models.ImageField(upload_to='image',null=True,blank=False)
    price=models.IntegerField(null=True,blank=False)