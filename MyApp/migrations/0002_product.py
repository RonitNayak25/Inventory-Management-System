# Generated by Django 3.0.5 on 2020-07-16 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
