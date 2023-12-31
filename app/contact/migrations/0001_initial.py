# Generated by Django 4.2.7 on 2023-12-04 06:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactTag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tag', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tag')),
            ],
            options={
                'verbose_name': 'Kontakt Tag',
                'verbose_name_plural': 'Kontakt Tags',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Kontakt Name')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefon')),
                ('email', models.CharField(blank=True, max_length=50, null=True, verbose_name='Email')),
                ('address', models.CharField(blank=True, max_length=50, null=True, verbose_name='Adresse')),
                ('comment', models.CharField(blank=True, max_length=50, null=True, verbose_name='Bemerkungen')),
                ('tag_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contact.contacttag', verbose_name='Tag')),
            ],
            options={
                'verbose_name': 'Kontakt',
                'verbose_name_plural': 'Kontakte',
            },
        ),
    ]
