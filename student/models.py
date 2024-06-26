from django.db import models


class Student(models.Model):
    class Gender(models.TextChoices):
        male = 'М', 'Мужской'
        female = 'Ж', 'Женский'

    name = models.CharField(max_length=30, blank=False)
    surname = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=Gender.choices)
    parents_phone = models.CharField(max_length=100)
    parents_email = models.EmailField(max_length=100, blank=False)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    courses = models.ManyToManyField('course.Course', through='StudentCourse', related_name='students_course')

    def __str__(self):
        return f"{self.surname} {self.name} {self.last_name}"

    class Meta:
        ordering = ['surname', 'name', 'last_name']


class StudentCourse(models.Model):
    student = models.ForeignKey('Student', blank=True, null=True, on_delete=models.CASCADE)
    course = models.ForeignKey('course.Course', blank=True, null=True, on_delete=models.CASCADE)
