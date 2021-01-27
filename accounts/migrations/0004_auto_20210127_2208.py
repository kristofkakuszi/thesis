# Generated by Django 3.1.5 on 2021-01-27 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_studentform'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentform',
            name='email',
        ),
        migrations.RemoveField(
            model_name='studentform',
            name='lastname',
        ),
        migrations.AlterField(
            model_name='studentform',
            name='firstname',
            field=models.CharField(max_length=50, verbose_name='Enter name'),
        ),
    ]