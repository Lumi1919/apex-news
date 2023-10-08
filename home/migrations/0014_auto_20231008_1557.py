# Generated by Django 3.2.9 on 2023-10-08 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20231007_1355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='body',
        ),
        migrations.AddField(
            model_name='event',
            name='body1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='body2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='body3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='event',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='event',
            name='legende',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='legende2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='legende3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='a_voir',
            name='categorie',
            field=models.CharField(choices=[('activite', 'activite'), ('societe', 'societe'), ('sport', 'sport'), ('culture', 'culture')], max_length=255),
        ),
        migrations.AlterField(
            model_name='activite',
            name='i_d',
            field=models.CharField(blank=True, choices=[('spectacles', 'spactacles'), ('sorties', 'sorties'), ('visites', 'visites'), ('coup de coeur', 'coup de coeur')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='sport',
            name='i_d',
            field=models.CharField(blank=True, choices=[('lamb', 'lamb'), ('basket', 'basket'), ('tennis', 'tennis'), ('foot', 'foot'), ('autres', 'autres')], max_length=250, null=True),
        ),
    ]
