# Generated by Django 3.2.9 on 2023-10-13 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_auto_20231013_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='event',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='home.event'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='a_voir',
            name='categorie',
            field=models.CharField(choices=[('culture', 'culture'), ('societe', 'societe'), ('activite', 'activite'), ('sport', 'sport')], max_length=255),
        ),
        migrations.AlterField(
            model_name='activite',
            name='i_d',
            field=models.CharField(blank=True, choices=[('visites', 'visites'), ('coup de coeur', 'coup de coeur'), ('sorties', 'sorties'), ('spectacles', 'spactacles')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='article_categorie',
            field=models.CharField(blank=True, choices=[('sport', 'sport'), ('politique', 'politique'), ('monde', 'monde'), ('culture', 'culture'), ('business', 'business'), ('spiritualite', 'spiritualite'), ('societe', 'societe')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='sport',
            name='i_d',
            field=models.CharField(blank=True, choices=[('autres', 'autres'), ('lamb', 'lamb'), ('foot', 'foot'), ('basket', 'basket'), ('tennis', 'tennis')], max_length=250, null=True),
        ),
    ]
