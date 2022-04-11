# Generated by Django 4.0.3 on 2022-04-08 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_image_image_parkingspace_avg_rating_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parkingspace',
            name='images',
        ),
        migrations.AlterField(
            model_name='image',
            name='parkingSpace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='users.parkingspace'),
        ),
    ]
