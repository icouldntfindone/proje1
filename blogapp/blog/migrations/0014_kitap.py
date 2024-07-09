# Generated by Django 5.0.4 on 2024-04-29 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_job_sector'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kitap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=200)),
                ('yazar', models.CharField(max_length=100)),
                ('yayin_yili', models.IntegerField()),
                ('sayfa_sayisi', models.IntegerField()),
                ('olusturulma_tarihi', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]