# Generated by Django 2.2.6 on 2019-11-06 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Belt_review_app', '0002_auto_20191105_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='Belt_review_app.User'),
        ),
    ]
