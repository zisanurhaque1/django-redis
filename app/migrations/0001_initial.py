# Generated by Django 5.1.1 on 2024-10-08 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_social', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('likes_count', models.FloatField()),
                ('comments_count', models.FloatField()),
                ('views_count', models.FloatField()),
                ('input_text', models.CharField(max_length=244)),
                ('author_meta', models.CharField(max_length=244)),
                ('creation_date', models.CharField(max_length=244)),
            ],
        ),
    ]
