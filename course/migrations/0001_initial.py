# Generated by Django 4.2.7 on 2024-03-25 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('duration', models.IntegerField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CourseType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_1', models.CharField(max_length=255)),
                ('task_2', models.CharField(max_length=255)),
                ('task_3', models.CharField(max_length=255)),
                ('task_4', models.CharField(max_length=255)),
                ('answer_1', models.CharField(max_length=255)),
                ('answer_2', models.CharField(max_length=255)),
                ('answer_3', models.CharField(max_length=255)),
                ('answer_4', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('date', models.DateTimeField()),
                ('duration', models.IntegerField()),
                ('video_link', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='StudentHomework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_1', models.CharField(max_length=255)),
                ('answer_2', models.CharField(max_length=255)),
                ('answer_3', models.CharField(max_length=255)),
                ('answer_4', models.CharField(max_length=255)),
                ('total_grade', models.IntegerField(blank=True, null=True)),
                ('watch_lesson', models.BooleanField(default=False)),
                ('homework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.homework')),
            ],
        ),
    ]
