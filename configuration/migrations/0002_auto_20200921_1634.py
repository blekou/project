# Generated by Django 2.2.12 on 2020-09-21 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='status',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
