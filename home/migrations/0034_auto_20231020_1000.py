# Generated by Django 3.2.9 on 2023-10-20 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_auto_20231020_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='a_voir',
            name='categorie',
            field=models.CharField(choices=[('culture', 'culture'), ('activite', 'activite'), ('sport', 'sport'), ('societe', 'societe')], max_length=255),
        ),
        migrations.AlterField(
            model_name='activite',
            name='i_d',
            field=models.CharField(blank=True, choices=[('visites', 'visites'), ('spectacles', 'spactacles'), ('coup de coeur', 'coup de coeur'), ('sorties', 'sorties')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='article_categorie',
            field=models.CharField(blank=True, choices=[('video', 'video'), ('culture', 'culture'), ('sport', 'sport'), ('actualite', 'actualite'), ('politique', 'politique'), ('spiritualite', 'spiritualite'), ('homme_de_la_semaine', 'homme_de_la_semaine'), ('breaking', 'breaking'), ('societe', 'societe'), ('evenement', 'evenement'), ('activite', 'activite'), ('international', 'international'), ('business', 'business')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='sport',
            name='i_d',
            field=models.CharField(blank=True, choices=[('autres', 'autres'), ('basket', 'basket'), ('foot', 'foot'), ('lamb', 'lamb'), ('tennis', 'tennis')], max_length=250, null=True),
        ),
    ]
