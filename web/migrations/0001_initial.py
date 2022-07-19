# Generated by Django 4.0.4 on 2022-05-25 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
                ('icon', models.CharField(max_length=50)),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name': 'Social',
                'verbose_name_plural': 'Sociaux',
            },
        ),
    ]