# Generated by Django 3.2.9 on 2023-10-26 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0040_auto_20231020_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='a_voir',
            name='categorie',
            field=models.CharField(choices=[('activite', 'activite'), ('sport', 'sport'), ('culture', 'culture'), ('societe', 'societe')], max_length=255),
        ),
        migrations.AlterField(
            model_name='activite',
            name='i_d',
            field=models.CharField(blank=True, choices=[('visites', 'visites'), ('spectacles', 'spactacles'), ('sorties', 'sorties'), ('coup de coeur', 'coup de coeur')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='article_categorie',
            field=models.CharField(blank=True, choices=[('business', 'business'), ('culture', 'culture'), ('sport', 'sport'), ('breaking', 'breaking'), ('actualite', 'actualite'), ('politique', 'politique'), ('international', 'international'), ('activite', 'activite'), ('event', 'event'), ('evenement', 'evenement'), ('video', 'video'), ('homme_de_la_semaine', 'homme_de_la_semaine'), ('spiritualite', 'spiritualite'), ('societe', 'societe'), ('pub', 'pub')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='sport',
            name='i_d',
            field=models.CharField(blank=True, choices=[('lamb', 'lamb'), ('foot', 'foot'), ('autres', 'autres'), ('basket', 'basket'), ('tennis', 'tennis')], max_length=250, null=True),
        ),
    ]
