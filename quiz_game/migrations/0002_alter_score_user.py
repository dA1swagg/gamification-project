# Generated by Django 5.0.4 on 2024-05-02 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]
