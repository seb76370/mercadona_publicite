# Generated by Django 3.1.6 on 2023-05-10 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Promotions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datedebut', models.DateField()),
                ('datefin', models.DateField()),
                ('pourcentage', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Produits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('prix', models.FloatField(default=0.0)),
                ('images', models.FileField(upload_to='uploads/%Y/%m/%d/')),
                ('categorie', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Produits_Categories', to='products.categories')),
                ('promotions', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Produits_Promotions', to='products.promotions')),
            ],
        ),
    ]
