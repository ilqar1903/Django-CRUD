# Generated by Django 2.2.2 on 2019-06-26 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=120)),
                ('text', models.TextField()),
                ('create_date', models.DateTimeField()),
            ],
        ),
    ]