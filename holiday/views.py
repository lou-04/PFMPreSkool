from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Holiday


@login_required
def holiday_list(request):
    holidays = Holiday.objects.all()
    return render(request, 'holidays/holidays.html', {'holidays': holidays})


@login_required
def add_holiday(request):
    if request.method == 'POST':
        Holiday.objects.create(
            name=request.POST.get('name'),
            date=request.POST.get('date'),
            description=request.POST.get('description', ''),
        )
        messages.success(request, 'Holiday added.')
        return redirect('holiday_list')
    return render(request, 'holidays/add-holiday.html')


@login_required
def edit_holiday(request, pk):
    holiday = get_object_or_404(Holiday, pk=pk)
    if request.method == 'POST':
        holiday.name = request.POST.get('name')
        holiday.date = request.POST.get('date')
        holiday.description = request.POST.get('description', '')
        holiday.save()
        messages.success(request, 'Holiday updated.')
        return redirect('holiday_list')
    return render(request, 'holidays/edit-holiday.html', {'holiday': holiday})


@login_required
def delete_holiday(request, pk):
    holiday = get_object_or_404(Holiday, pk=pk)
    if request.method == 'POST':
        holiday.delete()
        messages.success(request, 'Holiday deleted.')
        return redirect('holiday_list')
    return render(request, 'holidays/confirm-delete.html', {'holiday': holiday})
