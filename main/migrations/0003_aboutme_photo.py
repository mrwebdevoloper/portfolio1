# Generated by Django 3.2.5 on 2021-09-29 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210929_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutme',
            name='photo',
            field=models.ImageField(null=True, upload_to='about'),
        ),
    ]