# Generated by Django 4.1.3 on 2022-12-01 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tesapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='checkedOut',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.CharField(default='diproses', max_length=30),
        ),
    ]