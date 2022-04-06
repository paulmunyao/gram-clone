from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
# Create your models here.


class images(models.Model):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length=50)
    image_caption = models.CharField(max_length=50)
    likes = models.ManyToManyField(User, related_name='likes')
    comments = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_caption(self):
        self.update()

class profile(models.Model):
    profile_photo = CloudinaryField('image')
    bio = models.TextField(max_length=100)
    profile_user = models.OneToOneField(User, on_delete=models.CASCADE)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, search_term):
        profiles = cls.objects.filter(
            profile_user__username__icontains=search_term)
        return profiles

    @classmethod
    def get_profile_by_id(cls, id):
        profile = cls.objects.get(profile_user__id=id)
        return profile

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

  