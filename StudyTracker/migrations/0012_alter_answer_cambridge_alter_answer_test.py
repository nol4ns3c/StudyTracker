# Generated by Django 4.2.6 on 2023-11-10 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IELTSer', '0011_alter_answer_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='Cambridge',
            field=models.CharField(choices=[('Cambridge 1', 'Cambridge 1'), ('Cambridge 2', 'Cambridge 2'), ('Cambridge 3', 'Cambridge 3'), ('Cambridge 4', 'Cambridge 4'), ('Cambridge 5', 'Cambridge 5'), ('Cambridge 6', 'Cambridge 6'), ('Cambridge 7', 'Cambridge 7'), ('Cambridge 8', 'Cambridge 8'), ('Cambridge 9', 'Cambridge 9'), ('Cambridge 10', 'Cambridge 10'), ('Cambridge 11', 'Cambridge 11'), ('Cambridge 12', 'Cambridge 12'), ('Cambridge 13', 'Cambridge 13'), ('Cambridge 14', 'Cambridge 14'), ('Cambridge 15', 'Cambridge 15'), ('Cambridge 16', 'Cambridge 16'), ('Cambridge 17', 'Cambridge 17'), ('Cambridge 18', 'Cambridge 18')], max_length=20),
        ),
        migrations.AlterField(
            model_name='answer',
            name='Test',
            field=models.CharField(choices=[('Test 1', 'Test 1'), ('Test 2', 'Test 2'), ('Test 3', 'Test 3'), ('Test 4', 'Test 4')], max_length=20),
        ),
    ]
