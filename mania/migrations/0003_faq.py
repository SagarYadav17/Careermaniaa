# Generated by Django 2.2 on 2021-01-04 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mania', '0002_auto_20201231_0500'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('answer', models.CharField(max_length=1000)),
            ],
        ),
    ]
