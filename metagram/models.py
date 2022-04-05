from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
# Create your models here.


class images(models.Model):
    image = CloudinaryField('image')
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
