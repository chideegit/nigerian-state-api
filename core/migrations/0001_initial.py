# Generated by Django 3.2.4 on 2021-08-02 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=100)),
                ('capital', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Governor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('state', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.state')),
            ],
        ),
    ]
