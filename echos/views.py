from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AddEchoForm, EditEchoForm
from .models import Echo


@login_required
def echo_list(request):
    echos = Echo.objects.all().order_by('-created_at')
    return render(request, 'echos/echo/echo_list.html', {'echos': echos})


@login_required
def echo_detail(request, pk):
    echo = get_object_or_404(Echo, pk=pk)
    waves = echo.waves.all().order_by('-created_at')[:5]
    return render(request, 'echos/echo/echo_detail.html', {'echo': echo, 'waves': waves})


@login_required
def add_echo(request):
    form = AddEchoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        echo = form.save(commit=False)
        echo.user = request.user
        echo.save()
        messages.success(request, 'Echo added successfully.')
        return redirect(echo.get_absolute_url())

    return render(request, 'echos/echo/add_echo.html', {'form': form})


@login_required
def edit_echo(request, pk):
    echo = get_object_or_404(Echo, pk=pk)

    if echo.user != request.user:
        return HttpResponseForbidden('You are not allowed to edit this echo.')

    form = EditEchoForm(request.POST or None, instance=echo)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Echo updated successfully.')
        return redirect(echo.get_absolute_url())

    return render(request, 'echos/echo/edit_echo.html', {'form': form, 'echo': echo})


@login_required
def delete_echo(request, pk):
    echo = get_object_or_404(Echo, pk=pk)

    if echo.user != request.user:
        return HttpResponseForbidden('You are not allowed to delete this echo.')

    if request.method == 'POST':
        echo.delete()
        messages.success(request, 'Echo deleted successfully.')
        return redirect('echos:echo_list')

    return render(request, 'echos/echo/delete_echo.html', {'echo': echo})


@login_required
def waves_echo(request, pk):
    echo = get_object_or_404(Echo, pk=pk)
    waves = echo.waves.all()
    return render(request, 'echos/echo/waves_echo.html', {'waves': waves, 'echo': echo})
