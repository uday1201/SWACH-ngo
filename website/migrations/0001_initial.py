# Generated by Django 2.0.6 on 2018-09-27 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='asha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='mother',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('age', models.IntegerField()),
                ('husband_name', models.CharField(max_length=150)),
                ('village', models.TextField()),
                ('district', models.TextField()),
                ('smartphone', models.BooleanField()),
                ('consent', models.BooleanField()),
                ('asha_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='website.asha')),
            ],
        ),
    ]
