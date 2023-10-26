# Generated by Django 3.2.9 on 2023-10-20 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0039_auto_20231020_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='a_voir',
            name='categorie',
            field=models.CharField(choices=[('societe', 'societe'), ('activite', 'activite'), ('culture', 'culture'), ('sport', 'sport')], max_length=255),
        ),
        migrations.AlterField(
            model_name='articles',
            name='article_categorie',
            field=models.CharField(blank=True, choices=[('actualite', 'actualite'), ('international', 'international'), ('sport', 'sport'), ('culture', 'culture'), ('evenement', 'evenement'), ('activite', 'activite'), ('societe', 'societe'), ('video', 'video'), ('homme_de_la_semaine', 'homme_de_la_semaine'), ('business', 'business'), ('politique', 'politique'), ('spiritualite', 'spiritualite'), ('breaking', 'breaking')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='sport',
            name='i_d',
            field=models.CharField(blank=True, choices=[('autres', 'autres'), ('lamb', 'lamb'), ('basket', 'basket'), ('tennis', 'tennis'), ('foot', 'foot')], max_length=250, null=True),
        ),
    ]
