# Generated by Django 3.1.3 on 2021-06-14 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget_amt', models.FloatField()),
                ('date', models.DateField()),
                ('category', models.CharField(max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='Income',
        ),
    ]
