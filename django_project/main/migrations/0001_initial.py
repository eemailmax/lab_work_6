# Generated by Django 5.0.4 on 2024-05-04 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(height_field='image_height', upload_to='', width_field='image_width')),
                ('image_width', models.IntegerField(default=0)),
                ('image_height', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastfile_path', models.CharField(max_length=255)),
            ],
        ),
    ]
