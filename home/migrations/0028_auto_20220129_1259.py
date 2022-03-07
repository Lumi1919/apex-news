# Generated by Django 3.2.9 on 2022-01-29 12:59

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_auto_20220129_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='a_voir',
            name='video',
            field=embed_video.fields.EmbedVideoField(),
        ),
        migrations.AlterField(
            model_name='activite',
            name='i_d',
            field=models.CharField(blank=True, choices=[('spectacles', 'spactacles'), ('sorties', 'sorties'), ('visites', 'visites')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='sport',
            name='i_d',
            field=models.CharField(blank=True, choices=[('foot', 'foot'), ('lamb', 'lamb'), ('tennis', 'tennis'), ('autres', 'autres'), ('basket', 'basket')], max_length=250, null=True),
        ),
    ]