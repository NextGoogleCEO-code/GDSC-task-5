from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import logout

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required

def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Save the user
            user = form.save()
            
            # Optionally, log the user in immediately
            login(request, user)
            
            # Redirect to the homepage (or any other page)
            return redirect('blog-index')  # 'homepage' should match the name in your URL config.
    else:
        form = SignUpForm()
    
    return render(request, 'users/sign_up.html', {'form': form})


def logout_view(request):
    """A customised logout page"""
    logout(request)
    return render(request, 'users/logout.html')
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profilemodel  # Verify that `profilemodel` is correct.
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('users-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profilemodel)
    
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    
    return render(request, 'users/profile.html', context)
