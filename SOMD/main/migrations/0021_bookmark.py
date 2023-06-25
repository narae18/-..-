# Generated by Django 4.2.1 on 2023-06-25 05:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0020_rename_is_pinned_post_is_fix'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('somd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookmarkeds', to='main.somd')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookmarkings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
