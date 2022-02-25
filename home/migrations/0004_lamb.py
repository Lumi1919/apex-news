# Generated by Django 3.2.9 on 2021-12-22 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_gamecomment_pronostic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lamb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intro', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.ImageField(upload_to='')),
                ('author', models.CharField(max_length=255)),
                ('author_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
