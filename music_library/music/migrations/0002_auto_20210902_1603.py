# Generated by Django 3.2.7 on 2021-09-02 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='genre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='song',
            name='release_date',
            field=models.DateTimeField(),
        ),
    ]
