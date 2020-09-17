from django.contrib import admin
from courselist.models import Course, Semester
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_title','course_last_updated')
    pass

class SemesterAdmin(admin.ModelAdmin):
    pass

admin.site.register(Course, CourseAdmin)
admin.site.register(Semester, SemesterAdmin)
