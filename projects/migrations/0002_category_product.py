# Generated by Django 2.0.4 on 2019-05-15 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('sort', models.IntegerField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('seedCode', models.TextField()),
                ('location', models.TextField()),
                ('credit', models.DecimalField(decimal_places=2, max_digits=6)),
                ('availableFrom', models.TextField()),
                ('availableTo', models.TextField()),
                ('status', models.TextField()),
            ],
        ),
    ]
