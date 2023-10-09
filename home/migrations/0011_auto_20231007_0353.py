# Generated by Django 3.2.9 on 2023-10-07 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20231006_1251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Politique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legende', models.CharField(blank=True, max_length=255, null=True)),
                ('legende2', models.CharField(blank=True, max_length=255, null=True)),
                ('legende3', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(max_length=255)),
                ('body1', models.TextField(blank=True, null=True)),
                ('body2', models.TextField(blank=True, null=True)),
                ('body3', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='')),
                ('author', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='a_voir',
            name='categorie',
            field=models.CharField(choices=[('activite', 'activite'), ('sport', 'sport'), ('societe', 'societe'), ('culture', 'culture')], max_length=255),
        ),
        migrations.AlterField(
            model_name='activite',
            name='i_d',
            field=models.CharField(blank=True, choices=[('visites', 'visites'), ('coup de coeur', 'coup de coeur'), ('spectacles', 'spactacles'), ('sorties', 'sorties')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='sport',
            name='i_d',
            field=models.CharField(blank=True, choices=[('foot', 'foot'), ('basket', 'basket'), ('autres', 'autres'), ('tennis', 'tennis'), ('lamb', 'lamb')], max_length=250, null=True),
        ),
    ]