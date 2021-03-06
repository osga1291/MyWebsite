# Generated by Django 3.0.6 on 2020-05-09 03:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=100)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.PositiveSmallIntegerField(choices=[(2, 'accept'), (3, 'deny'), (1, 'pending'), (4, 'confirmed')], default=1)),
                ('is_read', models.BooleanField(default=False)),
            ],
        ),
    ]
