from django.db import models


AVATAR_SIZE = (300, 100)


class Profile(models.Model):
    image = models.ImageField(upload_to='profile/image')
    avatar = models.ImageField(upload_to='profile/avatar', null=True)
    avatar_width = models.IntegerField(default=AVATAR_SIZE[0])
    avatar_height = models.IntegerField(default=AVATAR_SIZE[1])
    avatar_x = models.IntegerField(default=0)
    avatar_y = models.IntegerField(default=0)

    def get_absolute_url(self):
        return '/'
