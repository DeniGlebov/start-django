# Generated by Django 2.2.12 on 2020-05-23 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_logger_created'),
        ('group', '0004_auto_20200510_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='head',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.Student'),
        ),
    ]
