from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from student.models import Student
from teacher.models import Teacher
from department.models import Department
from subject.models import Subject
from holiday.models import Holiday
from exam.models import Exam


def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return redirect('login')


@login_required
def dashboard(request):
    today = timezone.now().date()
    context = {
        'student_count': Student.objects.count(),
        'teacher_count': Teacher.objects.count(),
        'department_count': Department.objects.count(),
        'subject_count': Subject.objects.count(),
        'upcoming_holidays': Holiday.objects.filter(date__gte=today).order_by('date')[:5],
        'upcoming_exams': Exam.objects.filter(exam_date__gte=today).order_by('exam_date')[:5],
    }
    return render(request, 'dashboard.html', context)
