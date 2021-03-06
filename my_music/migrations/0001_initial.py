# Generated by Django 2.1.4 on 2019-01-23 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MusicSheet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sheet_id', models.IntegerField()),
                ('music_id', models.IntegerField()),
            ],
            options={
                'db_table': 'music_sheet',
            },
        ),
        migrations.CreateModel(
            name='UserSheet',
            fields=[
                ('sheet_id', models.AutoField(primary_key=True, serialize=False)),
                ('sheet_name', models.CharField(max_length=20)),
                ('user_id', models.IntegerField()),
            ],
            options={
                'db_table': 'user_sheet',
            },
        ),
    ]
