# Generated by Django 3.2.9 on 2023-10-02 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20231002_0259'),
    ]

    operations = [
        migrations.AddField(
            model_name='societe',
            name='legende2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='societe',
            name='legende3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='a_voir',
            name='categorie',
            field=models.CharField(choices=[('culture', 'culture'), ('societe', 'societe'), ('sport', 'sport'), ('activite', 'activite')], max_length=255),
        ),
        migrations.AlterField(
            model_name='activite',
            name='i_d',
            field=models.CharField(blank=True, choices=[('spectacles', 'spactacles'), ('visites', 'visites'), ('sorties', 'sorties'), ('coup de coeur', 'coup de coeur')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='sport',
            name='i_d',
            field=models.CharField(blank=True, choices=[('basket', 'basket'), ('autres', 'autres'), ('foot', 'foot'), ('tennis', 'tennis'), ('lamb', 'lamb')], max_length=250, null=True),
        ),
    ]