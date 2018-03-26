# Generated by Django 2.0.2 on 2018-03-22 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Authorization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is active')),
            ],
        ),
        migrations.CreateModel(
            name='Bot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_key', models.CharField(max_length=255, unique=True, verbose_name='API_KEY')),
                ('chat_id', models.CharField(max_length=255, verbose_name='Id')),
                ('first_name', models.CharField(max_length=255, verbose_name='First name')),
                ('username', models.CharField(max_length=255, verbose_name='Username')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bots', to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
            ],
            options={
                'verbose_name': 'Bot',
                'verbose_name_plural': 'Bots',
            },
        ),
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=255, verbose_name='Token')),
                ('chat_id', models.CharField(max_length=255, null=True, verbose_name='User id')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='telegramuser', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.AddField(
            model_name='authorization',
            name='bot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authorizations', to='telegram_bots.Bot'),
        ),
        migrations.AddField(
            model_name='authorization',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='authorization', to='telegram_bots.TelegramUser'),
        ),
        migrations.AlterUniqueTogether(
            name='authorization',
            unique_together={('bot', 'user')},
        ),
    ]
