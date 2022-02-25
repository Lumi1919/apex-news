# Generated by Django 3.2.9 on 2022-01-25 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_auto_20220122_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activite',
            name='i_d',
            field=models.CharField(blank=True, choices=[('spectacles', 'spactacles'), ('sorties', 'sorties'), ('visites', 'visites')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='sport',
            name='i_d',
            field=models.CharField(blank=True, choices=[('foot', 'foot'), ('lamb', 'lamb'), ('basket', 'basket'), ('tennis', 'tennis'), ('autres', 'autres')], max_length=250, null=True),
        ),
    ]
