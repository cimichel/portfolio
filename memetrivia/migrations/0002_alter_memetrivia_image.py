# Generated by Django 4.2.7 on 2023-11-15 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memetrivia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memetrivia',
            name='image',
            field=models.FileField(blank=True, upload_to='memetrivia_img/'),
        ),
    ]
