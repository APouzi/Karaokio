# Generated by Django 4.0.1 on 2022-02-10 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0003_venue_created_by_venue_has_nft_venue_state_venue_zip_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venue',
            name='created_by',
        ),
    ]
