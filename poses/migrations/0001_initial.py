# Generated by Django 3.0.6 on 2020-12-17 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_name', models.CharField(max_length=50, unique=True)),
                ('display_name', models.CharField(max_length=50)),
                ('preferred_side', models.CharField(choices=[('NA', 'Not available'), ('LEFT', 'Left'), ('RIGHT', 'Right')], default='NA', max_length=10)),
                ('sideways', models.BooleanField(default=False)),
                ('sanskrit_name', models.CharField(max_length=50, null=True)),
                ('two_sided', models.BooleanField(default=False)),
            ],
        ),
    ]
