from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Exam, ExamResult
from subject.models import Subject
from student.models import Student


@login_required
def exam_list(request):
    exams = Exam.objects.select_related('subject').all()
    return render(request, 'exams/exams.html', {'exams': exams})


@login_required
def add_exam(request):
    subjects = Subject.objects.all()
    if request.method == 'POST':
        Exam.objects.create(
            name=request.POST.get('name'),
            subject_id=request.POST.get('subject'),
            exam_date=request.POST.get('exam_date'),
            total_marks=request.POST.get('total_marks', 100),
            pass_marks=request.POST.get('pass_marks', 40),
        )
        messages.success(request, 'Exam added.')
        return redirect('exam_list')
    return render(request, 'exams/add-exam.html', {'subjects': subjects})


@login_required
def edit_exam(request, pk):
    exam = get_object_or_404(Exam, pk=pk)
    subjects = Subject.objects.all()
    if request.method == 'POST':
        exam.name = request.POST.get('name')
        exam.subject_id = request.POST.get('subject')
        exam.exam_date = request.POST.get('exam_date')
        exam.total_marks = request.POST.get('total_marks', 100)
        exam.pass_marks = request.POST.get('pass_marks', 40)
        exam.save()
        messages.success(request, 'Exam updated.')
        return redirect('exam_list')
    return render(request, 'exams/edit-exam.html', {'exam': exam, 'subjects': subjects})


@login_required
def delete_exam(request, pk):
    exam = get_object_or_404(Exam, pk=pk)
    if request.method == 'POST':
        exam.delete()
        messages.success(request, 'Exam deleted.')
        return redirect('exam_list')
    return render(request, 'exams/confirm-delete.html', {'exam': exam})


@login_required
def exam_results(request, pk):
    exam = get_object_or_404(Exam, pk=pk)
    results = ExamResult.objects.filter(exam=exam).select_related('student')
    students_without_result = Student.objects.exclude(
        id__in=results.values_list('student_id', flat=True)
    )
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        marks = request.POST.get('marks_obtained', 0)
        remarks = request.POST.get('remarks', '')
        ExamResult.objects.update_or_create(
            exam=exam, student_id=student_id,
            defaults={'marks_obtained': marks, 'remarks': remarks}
        )
        messages.success(request, 'Result saved.')
        return redirect('exam_results', pk=pk)
    return render(request, 'exams/exam-results.html', {
        'exam': exam, 'results': results,
        'students_without_result': students_without_result,
    })
