# Generated by Django 4.0.2 on 2022-02-07 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_client', '0005_remove_webhook_user_universe_constraint_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=40)),
            ],
        ),
    ]
