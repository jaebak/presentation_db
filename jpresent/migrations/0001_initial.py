# Generated by Django 4.2.14 on 2024-07-27 16:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('author', models.CharField(blank=True, max_length=200, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('pdf_url_link', models.URLField(blank=True, null=True)),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to='pdf_files/')),
                ('tag', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]