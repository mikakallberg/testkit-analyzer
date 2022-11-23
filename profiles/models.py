""" Model for User profile """
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Profile(models.Model):
    """ Elements for User profile """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_xx821h'
    )

    def __str__(self):
        return f"{self.owner}'s profile"
    
    def create_profile(sender, instance, created, **kwargs):
        """ Creating profile """
        if created:
            Profile.objects.create(owner=instance)
        
    post_save.connect(create_profile, sender=User)
