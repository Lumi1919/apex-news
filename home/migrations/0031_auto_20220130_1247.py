# Generated by Django 3.2.9 on 2022-01-30 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_auto_20220129_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='Breaking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='activite',
            name='i_d',
            field=models.CharField(blank=True, choices=[('sorties', 'sorties'), ('spectacles', 'spactacles'), ('visites', 'visites')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='sport',
            name='i_d',
            field=models.CharField(blank=True, choices=[('tennis', 'tennis'), ('lamb', 'lamb'), ('autres', 'autres'), ('basket', 'basket'), ('foot', 'foot')], max_length=250, null=True),
        ),
    ]