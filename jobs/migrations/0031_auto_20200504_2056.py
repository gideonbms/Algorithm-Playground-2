# Generated by Django 3.0.4 on 2020-05-04 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0030_auto_20200504_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyjob',
            name='education',
            field=models.IntegerField(choices=[(40, 'Master Degree'), (30, 'Bachelor Degree'), (20, 'High School Diploma'), (10, 'A Level')], default=''),
        ),
        migrations.AlterField(
            model_name='applyjob',
            name='location',
            field=models.IntegerField(choices=[(70, '5 to 10 miles away'), (60, '11 to 20 miles away'), (50, '21 to 30 miles away'), (40, '31 to 40 miles away'), (30, '41 to 50 miles away'), (20, '51 to  and above miles away')], default=''),
        ),
        migrations.AlterField(
            model_name='applyjob',
            name='name',
            field=models.CharField(choices=[('E', 'Elly Morrison'), ('A', 'Avik Amble'), ('B', 'Benson Adebayo')], default='', max_length=100),
        ),
    ]