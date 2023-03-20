# Generated by Django 4.1 on 2023-03-20 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=200)),
                ('recipe_pub_date', models.DateTimeField(verbose_name='date published')),
                ('ingredients_list', models.TextField(verbose_name='ingredients list')),
                ('recipe_instructions', models.TextField(verbose_name='recipe method')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_type', models.CharField(choices=[('V', 'Vegetarian'), ('NV', 'Non Vegetarian'), ('VG', 'Vegan')], default='', max_length=2)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipebook.recipe')),
            ],
        ),
    ]
