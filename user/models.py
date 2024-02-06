from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    u_name=models.CharField(max_length=200)
    profile=models.ImageField(upload_to="profileimages",default="profile.jpg")
    dob=models.DateField(null=True)
    options=(   ("male","male"),
                ("female","female")
            )
    gender=models.CharField(max_length=200,choices=options,default="female")

    def __str__(self):
        return self.user.username
    
def create_profile(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        UserProfile.objects.create(user=instance)
post_save.connect(create_profile,sender=User)