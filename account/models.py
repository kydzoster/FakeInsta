from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    # allows to associate profiles with users, when user is deleted, his profile also gets deleted
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    # image field, requires Pillow to work
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'
