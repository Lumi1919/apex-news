# Generated by Django 3.2.9 on 2021-12-15 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_game_comment_gamecomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamecomment',
            name='pronostic',
            field=models.CharField(max_length=500),
        ),
    ]