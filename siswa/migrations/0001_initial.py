# Generated by Django 4.1 on 2022-12-05 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='datasiswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('NISN', models.CharField(max_length=40)),
                ('tanggal_lahir', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('alamat', models.CharField(max_length=40)),
                ('jenis_kelamin', models.CharField(max_length=40)),
            ],
        ),
    ]
