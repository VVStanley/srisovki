from PIL import Image

from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from utils.file import delete_file, get_extension


def upload_path(instance, filename):
    '''фомируем путь загрузки аватара'''
    avatar_path = 'users/' + str(instance) + '/avatar' + get_extension(filename)
    full_path = settings.MEDIA_ROOT + '/' + avatar_path
    delete_file(full_path)
    return avatar_path


class User(AbstractUser):
    ip = models.GenericIPAddressField(verbose_name='ИП адресс', null=True, blank=True)
    avatar = models.ImageField(
        verbose_name='Аватар', upload_to=upload_path, null=True, blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]
    )
    date_birthday = models.DateField(verbose_name='День рождения', null=True, blank=True)
    city = models.CharField(verbose_name='Город', max_length=150, null=True, blank=True)

    def get_avatar(self):
        if self.avatar:
            return self.avatar.url
        return f'{settings.STATIC_URL}img/avatar.jpg'

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

        avatar_width = 110
        avatar_height = 110

        if self.avatar:
            image = Image.open(self.avatar)
            (image_width, image_height) = image.size
            if image_width > avatar_width or image_height > avatar_height:
                image = image.resize([avatar_width, avatar_height], Image.ANTIALIAS)
                image.save(self.avatar.path, quality=90, optimize=True)
            image.close()
