# Generated by Django 3.2.7 on 2021-09-08 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Confirm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trashCheck', models.CharField(max_length=30)),
                ('imageSet', models.ImageField(default='defualt_image/unnamed.png', upload_to='')),
            ],
        ),
    ]
