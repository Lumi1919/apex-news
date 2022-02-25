# Generated by Django 3.2.9 on 2022-01-29 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_alter_sport_i_d'),
    ]

    operations = [
        migrations.CreateModel(
            name='A_voir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='')),
                ('author', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='activite',
            name='i_d',
            field=models.CharField(blank=True, choices=[('visites', 'visites'), ('spectacles', 'spactacles'), ('sorties', 'sorties')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='sport',
            name='i_d',
            field=models.CharField(blank=True, choices=[('basket', 'basket'), ('tennis', 'tennis'), ('lamb', 'lamb'), ('foot', 'foot'), ('autres', 'autres')], max_length=250, null=True),
        ),
    ]
