# Generated by Django 5.0.4 on 2024-05-02 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_game', '0004_alter_score_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
