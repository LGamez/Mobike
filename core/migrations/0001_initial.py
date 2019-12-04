# Generated by Django 2.2.4 on 2019-10-18 06:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portafolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proyecto', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('fecha_crea', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_publ', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]