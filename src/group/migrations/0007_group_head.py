# Generated by Django 2.2.12 on 2020-05-24 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_logger_created'),
        ('group', '0006_remove_group_head'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='head',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.Student'),
        ),
    ]
