# Generated by Django 3.2.5 on 2021-07-18 07:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('excerpt', models.CharField(blank=True, max_length=100, null=True)),
                ('content', models.TextField(null=True)),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', models.SlugField(max_length=250, unique_for_date='published')),
                ('status', models.CharField(choices=[('published', 'Published'), ('draft', 'Draft')], default='published', max_length=10)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_post', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='Blog.category')),
            ],
            options={
                'ordering': ('-published',),
            },
        ),
    ]
