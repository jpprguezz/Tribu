from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from echos.models import Echo

from .forms import EditWavesForm
from .models import Wave


def valid_user(func):
    def wrapper(*args, **kwargs):
        user = args[0].user
        wave = Wave.objects.get(pk=kwargs['wave_pk'])
        if user != wave.user:
            return HttpResponseForbidden('No puedes editar esto')
        return func(*args, **kwargs)

    return wrapper


@login_required
def add_wave(request, pk):
    echo = get_object_or_404(Echo, pk=pk)
    if request.method == 'POST':
        form = EditWavesForm(request.POST)
        if form.is_valid():
            wave = form.save(commit=False)
            wave.echo = echo
            wave.save()
            messages.success(request, 'Wave added successfully')
            return redirect('waves:wave_detail', wave.pk)
    else:
        form = EditWavesForm()
    return render(request, 'waves/add_wave.html', dict(echo=echo, form=form))


@login_required
@valid_user
def edit_wave(request, wave_pk: None):
    wave = get_object_or_404(Wave, pk=wave_pk)
    if request.method == 'POST':
        if (form := EditWavesForm(request.POST, instance=wave)).is_valid():
            wave = form.save(commit=False)
            wave.user = request.user
            wave.save()

            messages.success(request, 'Wave updated successfully')
            return redirect('echos:echo_list')
    else:
        form = EditWavesForm(instance=wave)
    return render(request, 'waves/edit_wave.html', dict(wave=wave, form=form))


@login_required
@valid_user
def delete_wave(request, wave_pk):
    wave = get_object_or_404(Wave, pk=wave_pk)

    if request.method == 'POST':
        wave.delete()
        messages.success(request, 'Wave deleted successfully')
        return redirect('waves:wave_detail')

    return render(request, 'waves/delete_wave.html', {'wave': wave})
