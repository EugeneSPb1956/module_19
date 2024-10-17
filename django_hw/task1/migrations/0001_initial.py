# Generated by Django 5.1.2 on 2024-10-12 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя покупателя')),
                ('balance', models.DecimalField(decimal_places=2, max_digits=11, null=True, verbose_name='Баланс')),
                ('age', models.IntegerField(verbose_name='Возраст')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название игры')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=11, null=True, verbose_name='Цена')),
                ('size', models.DecimalField(decimal_places=3, max_digits=15, null=True, verbose_name='Размер файлов игры')),
                ('description', models.TextField(verbose_name='Описание')),
                ('age_limited', models.BooleanField(default=False, verbose_name='Ограничение возраста 18+')),
                ('buyer', models.ManyToManyField(related_name='games', to='task1.buyer')),
            ],
        ),
    ]