# Generated by Django 3.2.6 on 2021-11-17 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lost',
            name='details',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]
