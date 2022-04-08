# Generated by Django 4.0.1 on 2022-04-08 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('venues', '0001_initial'),
        ('event', '0002_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='enduservenuefavoritelist',
            name='venues',
            field=models.ManyToManyField(to='venues.Venue'),
        ),
        migrations.AddField(
            model_name='endusereventsfavoritelist',
            name='events',
            field=models.ManyToManyField(to='event.Event'),
        ),
        migrations.AddField(
            model_name='endusereventsfavoritelist',
            name='userProfile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.userprofile'),
        ),
        migrations.AddField(
            model_name='enduser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='enduser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
