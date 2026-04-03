from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Teacher
from department.models import Department
from home_auth.decorators import admin_required


@login_required
def teacher_list(request):
    teachers = Teacher.objects.select_related('department').all()
    return render(request, 'teachers/teachers.html', {'teachers': teachers})


@login_required
@admin_required
def add_teacher(request):
    departments = Department.objects.all()
    if request.method == 'POST':
        dept_id = request.POST.get('department')
        Teacher.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            teacher_id=request.POST.get('teacher_id'),
            gender=request.POST.get('gender'),
            date_of_birth=request.POST.get('date_of_birth'),
            department_id=dept_id if dept_id else None,
            mobile_number=request.POST.get('mobile_number'),
            email=request.POST.get('email'),
            address=request.POST.get('address', ''),
            joining_date=request.POST.get('joining_date'),
            teacher_image=request.FILES.get('teacher_image'),
        )
        messages.success(request, 'Teacher added successfully.')
        return redirect('teacher_list')
    return render(request, 'teachers/add-teacher.html', {'departments': departments})


@login_required
def view_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, teacher_id=teacher_id)
    return render(request, 'teachers/teacher-details.html', {'teacher': teacher})


@login_required
@admin_required
def edit_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, teacher_id=teacher_id)
    departments = Department.objects.all()
    if request.method == 'POST':
        teacher.first_name = request.POST.get('first_name')
        teacher.last_name = request.POST.get('last_name')
        teacher.gender = request.POST.get('gender')
        teacher.date_of_birth = request.POST.get('date_of_birth')
        dept_id = request.POST.get('department')
        teacher.department_id = dept_id if dept_id else None
        teacher.mobile_number = request.POST.get('mobile_number')
        teacher.email = request.POST.get('email')
        teacher.address = request.POST.get('address', '')
        teacher.joining_date = request.POST.get('joining_date')
        if request.FILES.get('teacher_image'):
            teacher.teacher_image = request.FILES.get('teacher_image')
        teacher.save()
        messages.success(request, 'Teacher updated.')
        return redirect('teacher_list')
    return render(request, 'teachers/edit-teacher.html',
                  {'teacher': teacher, 'departments': departments})


@login_required
@admin_required
def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, teacher_id=teacher_id)
    if request.method == 'POST':
        teacher.delete()
        messages.success(request, 'Teacher deleted.')
        return redirect('teacher_list')
    return render(request, 'teachers/confirm-delete.html', {'teacher': teacher})
