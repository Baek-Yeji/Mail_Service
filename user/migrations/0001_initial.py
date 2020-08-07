# Generated by Django 3.0.8 on 2020-07-27 04:52

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
                ('user_id', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('user_name', models.CharField(max_length=10)),
                ('user_tel', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
