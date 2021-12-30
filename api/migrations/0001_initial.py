# Generated by Django 4.0 on 2021-12-28 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('username', models.EmailField(blank=True, max_length=500, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('street', models.CharField(max_length=128)),
                ('suite', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=128)),
                ('zipcode', models.CharField(max_length=128)),
                ('geo_lat', models.FloatField()),
                ('geo_lng', models.FloatField()),
                ('phone', models.CharField(max_length=128)),
                ('website', models.CharField(max_length=128)),
                ('company_name', models.CharField(max_length=128)),
                ('company_catchPhrase', models.CharField(max_length=128)),
                ('company_bs', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Todos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('completed', models.BooleanField(default=False)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.users')),
            ],
            options={
                'verbose_name_plural': 'Todos',
            },
        ),
    ]
