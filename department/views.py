from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Department


@login_required
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'departments/departments.html', {'departments': departments})


@login_required
def add_department(request):
    if request.method == 'POST':
        Department.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description', ''),
        )
        messages.success(request, 'Department added successfully.')
        return redirect('department_list')
    return render(request, 'departments/add-department.html')


@login_required
def edit_department(request, pk):
    dept = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        dept.name = request.POST.get('name')
        dept.description = request.POST.get('description', '')
        dept.save()
        messages.success(request, 'Department updated.')
        return redirect('department_list')
    return render(request, 'departments/edit-department.html', {'dept': dept})


@login_required
def delete_department(request, pk):
    dept = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        dept.delete()
        messages.success(request, 'Department deleted.')
        return redirect('department_list')
    return render(request, 'departments/confirm-delete.html', {'dept': dept})
