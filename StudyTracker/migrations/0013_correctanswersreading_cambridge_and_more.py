# Generated by Django 4.2.6 on 2023-11-10 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IELTSer', '0012_alter_answer_cambridge_alter_answer_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='correctanswersreading',
            name='Cambridge',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='correctanswersreading',
            name='Test',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='CorrectAnswers',
            field=models.TextField(max_length=700, null=True),
        ),
    ]
