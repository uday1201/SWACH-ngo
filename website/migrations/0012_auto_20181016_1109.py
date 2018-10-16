# Generated by Django 2.0.8 on 2018-10-16 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_auto_20181015_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='attachment',
            name='stage',
        ),
        migrations.AddField(
            model_name='audio',
            name='audio',
            field=models.ManyToManyField(to='website.Attachment'),
        ),
        migrations.AddField(
            model_name='audio',
            name='stage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.stage'),
        ),
    ]