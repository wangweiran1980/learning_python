# Generated by Django 2.0.5 on 2022-02-19 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=32)),
                ('gender', models.BooleanField(default=True)),
                ('age', models.IntegerField(default=18)),
                ('tel', models.CharField(max_length=32)),
                ('pwd', models.CharField(default='', max_length=512)),
                ('creaet_time', models.DateTimeField()),
            ],
        ),
    ]
