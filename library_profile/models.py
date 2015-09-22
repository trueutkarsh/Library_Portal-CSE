from django.db import models
from django.contrib.auth.models import User


class libprofile(models.Model):
    user=models.OneToOneField(User)
    
    def __unicode__(self):
        return self.user.username
    
    
    
User.profile=property(lambda u :libprofile.objects.get_or_create(user=u)[0])
    




# Create your models here.
