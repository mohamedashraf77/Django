# Generated by Django 3.1.2 on 2021-11-13 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(verbose_name='Description movie')),
                ('likes', models.IntegerField()),
                ('watch_count', models.IntegerField()),
                ('rate', models.PositiveIntegerField()),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('modification_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
