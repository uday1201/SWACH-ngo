# Generated by Django 2.1.2 on 2018-10-12 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20181009_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mother',
            name='lmp',
            field=models.DateField(verbose_name='lmp'),
        ),
    ]
