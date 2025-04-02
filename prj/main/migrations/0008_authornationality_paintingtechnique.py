# Generated by Django 5.1.7 on 2025-04-02 19:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_movementpainting'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorNationality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.author')),
                ('nationality', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.nationality')),
            ],
        ),
        migrations.CreateModel(
            name='PaintingTechnique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('painting', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.painting')),
                ('technique', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.technique')),
            ],
        ),
    ]
