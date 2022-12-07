# Generated by Django 4.1.2 on 2022-11-30 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_table1_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=16)),
                ('Age', models.IntegerField()),
                ('Place', models.CharField(max_length=16)),
                ('Email', models.EmailField(max_length=254)),
                ('Photo', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('Password', models.CharField(max_length=16)),
                ('ConfirmPassword', models.CharField(max_length=16)),
            ],
        ),
    ]