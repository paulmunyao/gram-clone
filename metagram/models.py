from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


class User(models.Model):
    email = models.EmailField(max_length=50)
    full_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    # save the user to the database

    def save_user(self):
        self.save()

    def delete_user(self):
        self.delete()

class images(models.Model):
    image = CloudinaryField('images/',default='')
    image_name = models.CharField(max_length=50)
    image_caption = models.CharField(max_length=50)
    

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

class comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(images, on_delete=models.CASCADE)
    comment = models.CharField(max_length=50)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()            

    


