# Generated by Django 3.2.9 on 2023-10-11 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_auto_20231011_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activite',
            name='i_d',
            field=models.CharField(blank=True, choices=[('spectacles', 'spactacles'), ('visites', 'visites'), ('coup de coeur', 'coup de coeur'), ('sorties', 'sorties')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='episode',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='episode',
            name='link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='episode',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='episode',
            name='topic',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sport',
            name='i_d',
            field=models.CharField(blank=True, choices=[('tennis', 'tennis'), ('autres', 'autres'), ('foot', 'foot'), ('lamb', 'lamb'), ('basket', 'basket')], max_length=250, null=True),
        ),
    ]