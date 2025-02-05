from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import logout

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # If you don't need to modify the instance before saving:
            form.save()
            # Or, if you need to modify before saving:
            # user = form.save(commit=False)
            # user.some_field = 'some_value'
            # user.save()
            return redirect('blog-index')
    else:
        form = SignUpForm()
        
    context = {
        'form': form,
    }
    return render(request, 'users/sign_up.html', context)

def logout_view(request):
    """A customised logout page"""
    logout(request)
    return render(request, 'users/logout.html')

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
