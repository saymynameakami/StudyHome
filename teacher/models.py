from django.db import models
from course.models import Subject


class Teacher(models.Model):
    class Gender(models.TextChoices):
        male = 'М', 'Мужской'
        female = 'Ж', 'Женский'
    name = models.CharField(max_length=30, blank=False)
    surname = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=Gender.choices)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)
    job = models.CharField(max_length=30)
    education = models.CharField(max_length=100)
    experience = models.IntegerField()
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to='teachers/', blank=True)
    courses = models.ManyToManyField('course.Course', through='TeacherCourse', related_name='teacher_course')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.surname} {self.name} {self.last_name}"

    class Meta:
        ordering = ['surname', 'name', 'last_name']


class TeacherCourse(models.Model):
    teacher = models.ForeignKey('Teacher', blank=True, null=True, on_delete=models.CASCADE)
    course = models.ForeignKey('course.Course', blank=True, null=True, on_delete=models.CASCADE)
