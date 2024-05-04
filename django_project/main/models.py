from django.db import models

class Picture(models.Model):
    # Поле для хранения изображения
    image = models.ImageField(width_field = 'image_width', height_field='image_height')
    # Поле для хранения ширины изображения
    image_width = models.IntegerField(default=0)
    # Поле для хранения высоты изображения
    image_height = models.IntegerField(default=0)

class UploadFile(models.Model):
    # Поле для хранения пути к последнему загруженному файлу
    lastfile_path = models.CharField(max_length=255)