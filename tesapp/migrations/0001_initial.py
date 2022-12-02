# Generated by Django 4.1.3 on 2022-12-01 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField()),
                ('checkedOut', models.BooleanField()),
                ('status', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CartContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartId', models.IntegerField()),
                ('menuId', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]