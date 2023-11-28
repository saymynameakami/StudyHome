from django.contrib import admin
from django.db import models
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Teacher, TeacherCourse
from django.utils.html import format_html
from django.conf import settings

class TeacherCourseInline(admin.TabularInline):
    model = TeacherCourse
    extra = 1

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['surname', 'name', 'last_name', 'age', 'gender', 'subject', 'job', 'education', 'experience', 'phone', 'description', 'thumbnail_image']
    inlines = [TeacherCourseInline]
    filter_vertical = ['course']
    formfield_overrides = {
        models.ManyToManyField: {'widget': FilteredSelectMultiple('Courses', is_stacked=False)},
    }

    def thumbnail_image(self, obj):
        if obj.image:
            image_url = obj.image.url
            absolute_url = '{}{}'.format(settings.MEDIA_URL, image_url)
            return format_html('<img src="{}" width="50" height="50" />'.format(absolute_url))
        else:
            return 'No image'

    thumbnail_image.short_description = 'Thumbnail'
    thumbnail_image.allow_tags = True
@admin.register(TeacherCourse)
class TeacherCourseAdmin(admin.ModelAdmin):
    list_display = ['teacher', 'course']


admin.site.register(Teacher, TeacherAdmin)