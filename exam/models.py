from django.db import models
from student.models import Student
from subject.models import Subject


class Exam(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='exams')
    exam_date = models.DateField()
    total_marks = models.PositiveIntegerField(default=100)
    pass_marks = models.PositiveIntegerField(default=40)

    def __str__(self):
        return f"{self.name} - {self.subject.name}"


class ExamResult(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='results')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='results')
    marks_obtained = models.PositiveIntegerField(default=0)
    remarks = models.CharField(max_length=200, blank=True)

    class Meta:
        unique_together = ('exam', 'student')

    def passed(self):
        return self.marks_obtained >= self.exam.pass_marks

    def __str__(self):
        return f"{self.student} - {self.exam.name}: {self.marks_obtained}"
