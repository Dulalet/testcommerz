# Generated by Django 4.0 on 2021-12-19 20:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=40)),
                ('position', models.TextField(max_length=10)),
                ('employment_date', models.DateField()),
                ('salary', models.IntegerField()),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee')),
            ],
        ),
    ]
