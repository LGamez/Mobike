# Generated by Django 2.0.9 on 2018-10-29 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misperris', '0015_auto_20181029_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoptante',
            name='ciudad',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='adoptante',
            name='region',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='adoptante',
            name='tipo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='contraseña',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='descripcion',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='perros',
            name='codigo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='perros',
            name='descripcion',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='perros',
            name='estado',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='perros',
            name='nombre',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='perros',
            name='raza',
            field=models.CharField(max_length=60),
        ),
    ]
