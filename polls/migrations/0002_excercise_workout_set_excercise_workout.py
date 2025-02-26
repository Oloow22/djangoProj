# Generated by Django 5.1.6 on 2025-02-12 06:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Excercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('excercise', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=3000)),
                ('date', models.DateTimeField(verbose_name='workout date')),
            ],
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reps', models.IntegerField()),
                ('weight', models.FloatField(blank=True, null=True)),
                ('excercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.excercise')),
            ],
        ),
        migrations.AddField(
            model_name='excercise',
            name='workout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.workout'),
        ),
    ]
