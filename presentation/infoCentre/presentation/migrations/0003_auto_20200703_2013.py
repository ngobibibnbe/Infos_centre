# Generated by Django 3.0.7 on 2020-07-03 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentation', '0002_auto_20200703_2011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kibana_frame',
            name='parents_frame',
        ),
        migrations.AddField(
            model_name='parent_frame',
            name='kibanas_frame',
            field=models.ManyToManyField(to='presentation.Kibana_frame'),
        ),
    ]