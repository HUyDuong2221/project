# Generated by Django 4.0.5 on 2022-06-30 13:30

from django.db import migrations, models
import django_quill.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='baiviet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tieude', models.CharField(blank=True, max_length=100)),
                ('noidung', django_quill.fields.QuillField(default='ici')),
            ],
        ),
    ]
