# Generated by Django 3.2.11 on 2022-01-29 08:55

from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_profile_phone_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True, verbose_name='Unique identifier')),
                ('image', sorl.thumbnail.fields.ImageField(blank=True, max_length=255, upload_to='banner_pics', verbose_name="Banner's image")),
                ('link', models.CharField(blank=True, max_length=255, null=True, verbose_name='External link')),
            ],
            options={
                'verbose_name': 'banner',
                'verbose_name_plural': 'banners',
                'ordering': ('slug',),
            },
        ),
        migrations.CreateModel(
            name='AlternativeImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='banner_pics', verbose_name='image')),
                ('banner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alternatives', to='home.banner', verbose_name='banner')),
            ],
            options={
                'verbose_name': 'alternative image',
                'verbose_name_plural': 'alternative images',
            },
        ),
    ]
