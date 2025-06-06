# Generated by Django 5.2 on 2025-04-19 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ip_address', models.CharField(max_length=15)),
                ('port', models.IntegerField(default=25565)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('is_online', models.BooleanField(default=False)),
                ('last_checked', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
