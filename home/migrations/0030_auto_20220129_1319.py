# Generated by Django 3.2.9 on 2022-01-29 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_auto_20220129_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='a_voir',
            name='video',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='activite',
            name='i_d',
            field=models.CharField(blank=True, choices=[('visites', 'visites'), ('sorties', 'sorties'), ('spectacles', 'spactacles')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='sport',
            name='i_d',
            field=models.CharField(blank=True, choices=[('autres', 'autres'), ('basket', 'basket'), ('tennis', 'tennis'), ('lamb', 'lamb'), ('foot', 'foot')], max_length=250, null=True),
        ),
    ]