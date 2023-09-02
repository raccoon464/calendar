# Generated by Django 3.2.4 on 2023-08-24 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='discord_username',
        ),
        migrations.RemoveField(
            model_name='user',
            name='partner',
        ),
        migrations.RemoveField(
            model_name='user',
            name='telegram_verification_code',
        ),
        migrations.RemoveField(
            model_name='user',
            name='telegram_verification_code_expired_at',
        ),
        migrations.RemoveField(
            model_name='user',
            name='unverified_telegram_username',
        ),
        migrations.DeleteModel(
            name='UserContactChange',
        ),
    ]
