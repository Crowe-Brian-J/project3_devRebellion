# Generated by Django 4.2.2 on 2023-06-22 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_feed_timestamp_feedcomment_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]