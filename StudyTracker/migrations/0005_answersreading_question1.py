# Generated by Django 4.2.6 on 2023-11-06 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IELTSer', '0004_answersreading'),
    ]

    operations = [
        migrations.AddField(
            model_name='answersreading',
            name='question1',
            field=models.CharField(max_length=20, null=True),
        ),
    ]