from django.contrib import admin
from .models import (Course, Enrollment, Announcement, Comment, Lesson, Material)

class CourseAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'start_date', 'create_at', 'update_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class MaterialInLineAdmin(admin.StackedInline):

    model = Material

class LessonAdmin(admin.ModelAdmin):

    list_display = ['name', 'number', 'course', 'release_date']
    search_fields = ['name', 'description']
    list_filter = ['create_at']
    inlines = [
        MaterialInLineAdmin
    ]

admin.site.register(Course, CourseAdmin)
admin.site.register([Enrollment, Announcement, Comment, Material])
admin.site.register(Lesson, LessonAdmin)
