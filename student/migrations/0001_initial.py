# Generated by Django 4.2.7 on 2024-03-25 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('М', 'Мужской'), ('Ж', 'Женский')], max_length=1)),
                ('parents_phone', models.CharField(max_length=100)),
                ('parents_email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='images/')),
            ],
            options={
                'ordering': ['surname', 'name', 'last_name'],
            },
        ),
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.course')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(related_name='students_course', through='student.StudentCourse', to='course.course'),
        ),
    ]
