# Generated by Django 5.0.4 on 2024-04-13 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_name', models.CharField(editable=False, max_length=100)),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
    ]