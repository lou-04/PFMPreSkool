from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import TimeTable
from subject.models import Subject
from teacher.models import Teacher


@login_required
def timetable_list(request):
    entries = TimeTable.objects.select_related('subject', 'teacher').all()
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    grouped = {day: entries.filter(day=day) for day in days}
    return render(request, 'timetable/timetable.html',
                  {'grouped': grouped, 'days': days, 'entries': entries})


@login_required
def add_timetable(request):
    subjects = Subject.objects.all()
    teachers = Teacher.objects.all()
    days = TimeTable.DAY_CHOICES
    if request.method == 'POST':
        TimeTable.objects.create(
            class_name=request.POST.get('class_name'),
            section=request.POST.get('section'),
            subject_id=request.POST.get('subject'),
            teacher_id=request.POST.get('teacher') or None,
            day=request.POST.get('day'),
            start_time=request.POST.get('start_time'),
            end_time=request.POST.get('end_time'),
        )
        messages.success(request, 'Timetable entry added.')
        return redirect('timetable_list')
    return render(request, 'timetable/add-timetable.html',
                  {'subjects': subjects, 'teachers': teachers, 'days': days})


@login_required
def edit_timetable(request, pk):
    entry = get_object_or_404(TimeTable, pk=pk)
    subjects = Subject.objects.all()
    teachers = Teacher.objects.all()
    days = TimeTable.DAY_CHOICES
    if request.method == 'POST':
        entry.class_name = request.POST.get('class_name')
        entry.section = request.POST.get('section')
        entry.subject_id = request.POST.get('subject')
        entry.teacher_id = request.POST.get('teacher') or None
        entry.day = request.POST.get('day')
        entry.start_time = request.POST.get('start_time')
        entry.end_time = request.POST.get('end_time')
        entry.save()
        messages.success(request, 'Timetable entry updated.')
        return redirect('timetable_list')
    return render(request, 'timetable/edit-timetable.html',
                  {'entry': entry, 'subjects': subjects, 'teachers': teachers, 'days': days})


@login_required
def delete_timetable(request, pk):
    entry = get_object_or_404(TimeTable, pk=pk)
    if request.method == 'POST':
        entry.delete()
        messages.success(request, 'Timetable entry deleted.')
        return redirect('timetable_list')
    return render(request, 'timetable/confirm-delete.html', {'entry': entry})
