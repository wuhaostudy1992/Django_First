# Generated by Django 2.0.2 on 2018-02-26 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='topic',
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
    ]
