# Generated by Django 4.1 on 2023-04-28 08:15

from django.db import migrations, models
import myproject.utils


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0003_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, max_length=255, upload_to=myproject.utils.uuid_name_upload_to),
        ),
    ]
