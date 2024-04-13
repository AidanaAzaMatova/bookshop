# Generated by Django 5.0.4 on 2024-04-13 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=30)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]