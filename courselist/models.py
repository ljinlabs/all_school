from django.db import models
import datetime

# Create your models here.
class Semester(models.Model):
    SEMESTER_CHOICES = [
        ('fa','Fall'),
        ('sp','Spring'),
        ('su','Summer')
    ]
    sem = models.CharField(max_length=10,choices=SEMESTER_CHOICES)

class Course(models.Model):
    course_semester_choices = [
        ('fa-2020','Fall 2020'),
        ('sp-2021','Spring 2021'),
        ('su-2021','Summer 2021'),
    ]
    course_title = models.CharField(max_length=20)
    course_lectures = models.URLField()
    course_forums = models.URLField()
    course_schedule = models.ForeignKey(Semester,on_delete=models.CASCADE)
    course_homework = models.URLField()
    course_labs = models.URLField()
    course_last_updated = models.DateTimeField(auto_now=True)
    course_created = models.DateTimeField(auto_now_add=True)
    course_semester = models.CharField(max_length=10,choices=course_semester_choices)

    # def is_current(self):
    #     return self.course_last_updated > datetime.date.today
