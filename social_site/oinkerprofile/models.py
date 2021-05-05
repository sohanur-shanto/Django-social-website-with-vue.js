from django.contrib.auth.models import User
from django.db import models

class OinkerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)
    avatar = models.ImageField(upload_to= 'static/images/', blank=True, null=True, default = 'avatar-2.jpg')

    
User.oinkerprofile = property(lambda u:OinkerProfile.objects.get_or_create(user=u)[0])

