# Generated by Django 4.1.3 on 2022-11-21 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0005_alter_match_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=''),
        ),
    ]
