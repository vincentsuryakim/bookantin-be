# Generated by Django 4.1.3 on 2022-12-04 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.CharField(choices=[('menunggu_pembayaran', 'menunggu_pembayaran'), ('diproses', 'diproses'), ('siap_diambil', 'siap_diambil')], default='menunggu_pembayaran', max_length=30),
        ),
    ]
