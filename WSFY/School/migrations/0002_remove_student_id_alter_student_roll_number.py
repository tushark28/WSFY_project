# Generated by Django 4.2.3 on 2023-07-30 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_number',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
