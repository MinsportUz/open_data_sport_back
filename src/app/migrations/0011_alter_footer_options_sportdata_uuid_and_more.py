# Generated by Django 4.2.7 on 2024-01-19 06:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_footer_twitter_alter_footer_facebook_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='footer',
            options={'verbose_name': 'Footer [saytni pastgi qismi]', 'verbose_name_plural': 'Footer [saytni pastgi qismi]'},
        ),
        migrations.AddField(
            model_name='sportdata',
            name='uuid',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True, verbose_name='UUID'),
        ),
        migrations.AlterField(
            model_name='footer',
            name='facebook',
            field=models.URLField(blank=True, null=True, verbose_name='Facebook manzili'),
        ),
        migrations.AlterField(
            model_name='footer',
            name='instagram',
            field=models.URLField(blank=True, null=True, verbose_name='Instagram manzili'),
        ),
        migrations.AlterField(
            model_name='footer',
            name='phone',
            field=models.CharField(max_length=255, verbose_name='Telefon raqamlar'),
        ),
        migrations.AlterField(
            model_name='footer',
            name='telegram',
            field=models.URLField(blank=True, null=True, verbose_name='Telegram manzili'),
        ),
        migrations.AlterField(
            model_name='footer',
            name='youtube',
            field=models.URLField(blank=True, null=True, verbose_name='Youtube manzili'),
        ),
    ]
