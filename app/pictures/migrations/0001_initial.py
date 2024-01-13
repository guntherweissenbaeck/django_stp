# Generated by Django 5.0.1 on 2024-01-13 14:13

import django.db.models.deletion
import pictures.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bird', '0002_alter_fallenbird_diagnosis_doctor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to=pictures.models.upload_filename)),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('fallenbird', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bird.fallenbird')),
            ],
            options={
                'verbose_name': 'Bild',
                'verbose_name_plural': 'Bilder',
            },
        ),
    ]
