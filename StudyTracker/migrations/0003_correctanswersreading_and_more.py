# Generated by Django 4.2.6 on 2023-11-06 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IELTSer', '0002_telebe'),
    ]

    operations = [
        migrations.CreateModel(
            name='CorrectAnswersReading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='CorrectAnswers',
            new_name='CorrectAnswersListening',
        ),
        migrations.DeleteModel(
            name='telebe',
        ),
    ]
