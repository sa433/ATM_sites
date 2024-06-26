# Generated by Django 3.2.25 on 2024-04-16 14:44

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
                ('sname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=50)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atm_management.state')),
            ],
        ),
        migrations.CreateModel(
            name='ATMSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=255)),
                ('bid', models.CharField(max_length=10)),
                ('baddress', models.TextField()),
                ('persondetail', models.JSONField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atm_management.city')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atm_management.state')),
            ],
        ),
    ]
