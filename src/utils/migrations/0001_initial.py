# Generated by Django 4.2.7 on 2024-01-09 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name="To'liq nomi [title]")),
                ('title_uz', models.CharField(max_length=255, null=True, verbose_name="To'liq nomi [title]")),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name="To'liq nomi [title]")),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name="To'liq nomi [title]")),
                ('attr', models.CharField(max_length=255, verbose_name='qisqa nomi [attr]')),
                ('attr_uz', models.CharField(max_length=255, null=True, verbose_name='qisqa nomi [attr]')),
                ('attr_en', models.CharField(max_length=255, null=True, verbose_name='qisqa nomi [attr]')),
                ('attr_ru', models.CharField(max_length=255, null=True, verbose_name='qisqa nomi [attr]')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan vaqti')),
            ],
            options={
                'verbose_name': 'Xolat',
                'verbose_name_plural': 'Xolatlar',
                'db_table': 'state',
            },
        ),
    ]
