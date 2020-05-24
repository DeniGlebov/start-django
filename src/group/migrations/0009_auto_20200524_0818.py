# Generated by Django 2.2.12 on 2020-05-24 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0009_auto_20200517_0827'),
        ('group', '0008_auto_20200524_0736'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='curator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='groups_curator', to='teachers.Teacher'),
        ),
        migrations.AlterField(
            model_name='group',
            name='head',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='groups_head', to='students.Student'),
        ),
    ]
