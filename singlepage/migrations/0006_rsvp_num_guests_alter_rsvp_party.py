# Generated by Django 5.0.3 on 2024-03-26 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singlepage', '0005_remove_rsvp_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='rsvp',
            name='num_guests',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='party',
            field=models.CharField(choices=[('Nhà Trai', 'Nhà Trai'), ('Nhà Gái', 'Nhà Gái'), ('Cả Hai', 'Cả Hai')], default='Cả Hai', max_length=10),
        ),
    ]