# Generated by Django 3.2.9 on 2023-10-20 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_auto_20231020_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='a_voir',
            name='categorie',
            field=models.CharField(choices=[('culture', 'culture'), ('sport', 'sport'), ('societe', 'societe'), ('activite', 'activite')], max_length=255),
        ),
        migrations.AlterField(
            model_name='activite',
            name='i_d',
            field=models.CharField(blank=True, choices=[('spectacles', 'spactacles'), ('visites', 'visites'), ('sorties', 'sorties'), ('coup de coeur', 'coup de coeur')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='article_categorie',
            field=models.CharField(blank=True, choices=[('breaking', 'breaking'), ('spiritualite', 'spiritualite'), ('actualite', 'actualite'), ('international', 'international'), ('activite', 'activite'), ('homme_de_la_semaine', 'homme_de_la_semaine'), ('sport', 'sport'), ('business', 'business'), ('societe', 'societe'), ('politique', 'politique'), ('video', 'video'), ('evenement', 'evenement'), ('culture', 'culture')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='sport',
            name='i_d',
            field=models.CharField(blank=True, choices=[('basket', 'basket'), ('tennis', 'tennis'), ('autres', 'autres'), ('lamb', 'lamb'), ('foot', 'foot')], max_length=250, null=True),
        ),
    ]