from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Product(models.Model):
    produc_id = models.AutoField
    product_name= models.CharField(max_length=50)
    category = models.CharField(max_length=50, default='')
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=50)
    pub_date = models.DateField()
    images = models.ImageField(upload_to="", default='')
    product_banner_image = models.ImageField(upload_to= './banner',default='')

    def __str__(self):
        return self.product_name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='./profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            outpu_size = (300, 300)
            img.thumbnail(outpu_size)
            img.save(self.image.path)


