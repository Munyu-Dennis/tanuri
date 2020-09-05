from django.db import models
from django.utils import timezone
from PIL import Image

class Menu(models.Model):
    img = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=255)
    breakfast = models.BooleanField(default=False)
    lunch = models.BooleanField(default=False)
    dinner = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    offerprice = models.IntegerField(blank=True, default=0)
    
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image = Image.open(self.img.path) 
        if image.height > 300 and image.width > 300:
            output_size = (300, 300)
            image.thumbnail(output_size)
            image.save(self.img.path)
class Oder(models.Model):
    from .models import Menu
    meal = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    phone_number = models.IntegerField()
    def __str__(self):
        return f' {self.name} {self.phone_number}'
    

class Team(models.Model):
    imgt = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=150)
    little_info = models.TextField(blank=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image = Image.open(self.imgt.path) 
        if image.height > 300 and image.width > 300:
            output_size = (300, 300)
            image.thumbnail(output_size)
            image.save(self.imgt.path)
    

class Review(models.Model):
    myphoto = models.ImageField(default='static/default.png', upload_to='pics')
    name = models.CharField(max_length=150)
    your_experience = models.TextField()
    facebook = models.CharField(max_length=150, blank=True)
    twitter = models.CharField(max_length=150, blank=True)
    instagram  =  models.CharField(max_length=150, blank=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.myphoto.path) 
        if img.height > 300 and img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.myphoto.path)
    

class Blog(models.Model):
    imgb = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=150)
    date_posted = models.DateTimeField( default=timezone.now)
    slug = models.CharField(max_length=300,default='')
    content = models.TextField()
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image = Image.open(self.imgb.path) 
        if image.height > 300 and image.width > 300:
            output_size = (300, 300)
            image.thumbnail(output_size)
            image.save(self.imgb.path)
    def get_pk(self):
        p_k = {"pk" : self.pk}
        return p_k
    def get_absolute_url(self):
        p_k = self.get_pk()
        return reverse('blogdet', kwargs=p_k)
class Contant(models.Model):
    your_name = models.CharField(max_length=150)
    email = models.EmailField(default='')
    subject = models.CharField(max_length=300)
    message = models.TextField()
