# Generated by Django 5.0.6 on 2024-05-16 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_sections_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sections',
            name='img',
            field=models.ImageField(default='static/assets/img/menu/menu-item-1.png', upload_to='static/assets/img/menu/'),
        ),
    ]
