# Generated by Django 4.1.3 on 2022-11-30 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactanos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Correo', models.CharField(max_length=50)),
                ('Mensaje', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Trabaja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Apellido', models.CharField(max_length=50)),
                ('Correo', models.EmailField(max_length=254)),
                ('URL_Linkedin', models.URLField()),
            ],
        ),
    ]