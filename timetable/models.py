from django.db import models
from subject.models import Subject
from teacher.models import Teacher


class TimeTable(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'),
    ]

    class_name = models.CharField(max_length=50)
    section = models.CharField(max_length=10)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='timetables')
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL,
                                null=True, blank=True, related_name='timetables')
    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        ordering = ['day', 'start_time']

    def __str__(self):
        return f"{self.class_name} {self.section} - {self.subject.name} ({self.day})"
