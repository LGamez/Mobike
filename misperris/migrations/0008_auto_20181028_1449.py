# Generated by Django 2.0.9 on 2018-10-28 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misperris', '0007_auto_20181026_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=60),
        ),
    ]
