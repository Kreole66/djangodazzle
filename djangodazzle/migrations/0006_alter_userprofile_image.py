# Generated by Django 4.2.7 on 2023-12-01 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangodazzle', '0005_remove_recipe_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='user_images/'),
        ),
    ]