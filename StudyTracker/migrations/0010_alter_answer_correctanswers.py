# Generated by Django 4.2.6 on 2023-11-07 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IELTSer', '0009_answer_delete_answers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='CorrectAnswers',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
