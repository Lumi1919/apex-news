# Generated by Django 3.2.9 on 2023-10-03 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20231003_2350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activite',
            name='body',
        ),
        migrations.AddField(
            model_name='activite',
            name='body1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='activite',
            name='body2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='activite',
            name='body3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='activite',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='activite',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='activite',
            name='legende',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='activite',
            name='legende2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='activite',
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
            field=models.CharField(blank=True, choices=[('sorties', 'sorties'), ('spectacles', 'spactacles'), ('visites', 'visites'), ('coup de coeur', 'coup de coeur')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='sport',
            name='i_d',
            field=models.CharField(blank=True, choices=[('basket', 'basket'), ('tennis', 'tennis'), ('lamb', 'lamb'), ('autres', 'autres'), ('foot', 'foot')], max_length=250, null=True),
        ),
    ]
