from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from echos.models import Echo
from waves.models import Wave

from .forms import EditProfileForm
from .models import Profile


@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user/users_list.html', {'users': users})


@login_required
def user_logged(request):
    username = request.user.username
    return redirect('users:user_detail', username=username)


@login_required
def user_detail(request, username: str):
    user = get_object_or_404(User, username=username)
    echos = Echo.objects.filter(user=user).order_by('-created_at')[:5]
    total_echos = Echo.objects.filter(user=user).count()
    total_waves = Wave.objects.filter(user=user).count()

    return render(
        request,
        'users/user/user_detail.html',
        {'user': user, 'echos': echos, 'total_echos': total_echos, 'total_waves': total_waves},
    )


@login_required
def user_echos(request, username: str):
    user = get_object_or_404(User, username=username)
    echos = Echo.objects.filter(user=user).order_by('-created_at')

    return render(request, 'users/user/user_echos.html', {'user': user, 'echos': echos})


@login_required
def edit_profile(request, username: str):
    user = get_object_or_404(User, username=username)

    if request.user != user:
        return HttpResponseForbidden('No puedes editar este perfil')

    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('users:user_logged')
    else:
        form = EditProfileForm(instance=profile)

    return render(request, 'users/user/edit_profile.html', {'form': form, 'profile': profile})
