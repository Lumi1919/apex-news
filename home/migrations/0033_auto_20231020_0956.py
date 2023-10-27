# Generated by Django 3.2.9 on 2023-10-20 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_auto_20231019_1522'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment_Actu',
            new_name='Comment_Article',
        ),
        migrations.RemoveField(
            model_name='comment_article',
            name='actu',
        ),
        migrations.AddField(
            model_name='comment_article',
            name='article',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='home.articles'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='a_voir',
            name='categorie',
            field=models.CharField(choices=[('culture', 'culture'), ('sport', 'sport'), ('activite', 'activite'), ('societe', 'societe')], max_length=255),
        ),
        migrations.AlterField(
            model_name='articles',
            name='article_categorie',
            field=models.CharField(blank=True, choices=[('culture', 'culture'), ('spiritualite', 'spiritualite'), ('societe', 'societe'), ('international', 'international'), ('breaking', 'breaking'), ('activite', 'activite'), ('homme_de_la_semaine', 'homme_de_la_semaine'), ('business', 'business'), ('video', 'video'), ('actualite', 'actualite'), ('evenement', 'evenement'), ('politique', 'politique'), ('sport', 'sport')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='sport',
            name='i_d',
            field=models.CharField(blank=True, choices=[('foot', 'foot'), ('tennis', 'tennis'), ('basket', 'basket'), ('autres', 'autres'), ('lamb', 'lamb')], max_length=250, null=True),
        ),
    ]