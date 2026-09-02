from django.db import models

# Create your models here.


class Product(models.Model):
       category = models.ForeignKey('Category',on_delete=models.CASCADE,related_name='product',null=True,blank=True)
       name =models.CharField(max_length=100)
       description=models.TextField()
       price= models.DecimalField(max_digits=50,decimal_places=2)
       image=models.ImageField(upload_to='products/',null=True,blank=True)
       created=models.DateTimeField(auto_now_add=True,null=True,blank=True)

       def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

   