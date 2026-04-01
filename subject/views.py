from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Subject
from department.models import Department
from teacher.models import Teacher


@login_required
def subject_list(request):
    subjects = Subject.objects.select_related('department', 'teacher').all()
    return render(request, 'subjects/subjects.html', {'subjects': subjects})


@login_required
def add_subject(request):
    departments = Department.objects.all()
    teachers = Teacher.objects.all()
    if request.method == 'POST':
        Subject.objects.create(
            name=request.POST.get('name'),
            code=request.POST.get('code'),
            department_id=request.POST.get('department') or None,
            teacher_id=request.POST.get('teacher') or None,
            description=request.POST.get('description', ''),
        )
        messages.success(request, 'Subject added successfully.')
        return redirect('subject_list')
    return render(request, 'subjects/add-subject.html',
                  {'departments': departments, 'teachers': teachers})


@login_required
def edit_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    departments = Department.objects.all()
    teachers = Teacher.objects.all()
    if request.method == 'POST':
        subject.name = request.POST.get('name')
        subject.code = request.POST.get('code')
        subject.department_id = request.POST.get('department') or None
        subject.teacher_id = request.POST.get('teacher') or None
        subject.description = request.POST.get('description', '')
        subject.save()
        messages.success(request, 'Subject updated.')
        return redirect('subject_list')
    return render(request, 'subjects/edit-subject.html',
                  {'subject': subject, 'departments': departments, 'teachers': teachers})


@login_required
def delete_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        subject.delete()
        messages.success(request, 'Subject deleted.')
        return redirect('subject_list')
    return render(request, 'subjects/confirm-delete.html', {'subject': subject})
