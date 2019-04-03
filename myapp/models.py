from django.db import models
from django.utils import timezone

class UserInfo(models.Model):
    email=models.EmailField(max_length=255,primary_key=True)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    phonenumber=models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class CarInfo(models.Model):
    id_no=models.AutoField(primary_key=True)
    license_no=models.CharField(max_length=50)
    make=models.CharField(max_length=50)
    model=models.CharField(blank=True,max_length=50)
    year=models.IntegerField(blank=True)
    color=models.CharField(blank=True,max_length=50)
    engine=models.CharField(max_length=50)
    millage=models.CharField(max_length=50)
    trans=models.CharField(max_length=50)
    price=models.FloatField()
    date= models.DateField(default=timezone.now)
    owner=models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    car_image_1=models.ImageField(upload_to='car_images',blank=True,default='none.jpg')
    car_image_2=models.ImageField(upload_to='car_images',blank=True,default='none.jpg')
    car_image_3=models.ImageField(upload_to='car_images',blank=True,default='none.jpg')

class BlogTopics(models.Model):
    id =models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    text=models.TextField()
    author=models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    approved=models.TextField(default='no',max_length=3)

class Comments(models.Model):
    id =models.AutoField(primary_key=True)
    commenter=models.EmailField(max_length=255)
    blog_topic_id=models.ForeignKey(BlogTopics,on_delete=models.CASCADE)
    text=models.TextField()
    date= models.DateField(default=timezone.now)
