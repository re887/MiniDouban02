# Generated by Django 5.1.1 on 2024-09-20 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movie", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="movie",
            options={"verbose_name": "电影", "verbose_name_plural": "电影"},
        ),
        migrations.AlterField(
            model_name="movie",
            name="description",
            field=models.CharField(max_length=250, verbose_name="电影简介"),
        ),
        migrations.AlterField(
            model_name="movie",
            name="image",
            field=models.ImageField(upload_to="movie/images", verbose_name="电影海报"),
        ),
        migrations.AlterField(
            model_name="movie",
            name="title",
            field=models.CharField(max_length=100, verbose_name="电影名"),
        ),
        migrations.AlterField(
            model_name="movie",
            name="url",
            field=models.URLField(blank=True, verbose_name="电影资源"),
        ),
    ]
