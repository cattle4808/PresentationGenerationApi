# Generated by Django 5.2.4 on 2025-07-23 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('presentation_id', models.CharField(primary_key=True, serialize=False)),
                ('example', models.FileField(upload_to='presentation_examples/')),
                ('theme', models.CharField(max_length=100)),
                ('presentation', models.FileField(blank=True, null=True, upload_to='presentations/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
