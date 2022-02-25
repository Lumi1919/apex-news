# Generated by Django 3.2.9 on 2022-02-05 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_auto_20220201_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='a_voir',
            name='categorie',
            field=models.CharField(choices=[('societe', 'societe'), ('culture', 'culture'), ('activite', 'activite'), ('sport', 'sport')], max_length=255),
        ),
        migrations.AlterField(
            model_name='activite',
            name='i_d',
            field=models.CharField(blank=True, choices=[('coup de coeur', 'coup de coeur'), ('spectacles', 'spactacles'), ('sorties', 'sorties'), ('visites', 'visites')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='sport',
            name='i_d',
            field=models.CharField(blank=True, choices=[('foot', 'foot'), ('tennis', 'tennis'), ('basket', 'basket'), ('autres', 'autres'), ('lamb', 'lamb')], max_length=250, null=True),
        ),
    ]
