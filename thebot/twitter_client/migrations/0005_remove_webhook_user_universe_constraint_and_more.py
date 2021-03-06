# Generated by Django 4.0.2 on 2022-02-05 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_client', '0004_webhook_user_universe_constraint'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='webhook',
            name='user_universe_constraint',
        ),
        migrations.AddConstraint(
            model_name='webhook',
            constraint=models.UniqueConstraint(fields=('timerange_lower', 'timerange_upper'), name='timerange_constraint'),
        ),
    ]
