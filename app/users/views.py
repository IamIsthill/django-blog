from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# Custom form and fields
from .forms import UserRegister, UserUpdate, ProfileUpdate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout

# Create your views here.

def register_view(request):
  if request.method == "POST":
    form = UserRegister(request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      form.save()
      messages.success(request, f'Account has been created. You are now able to login, {username}!')
      return redirect('login')
      # form.save()
  else:
    form = UserRegister()
  return render(request, 'users/register.html', { 'form':form })

def login_view(request):
  if(request.method) == "POST":
    form = AuthenticationForm(data = request.POST)
    if(form.is_valid()):
      login(request, form.get_user())
      next_url = request.POST.get('next') or 'blog-home'  # Use 'blog-home' as default
      return redirect(next_url)
      # if 'next' in request.POST:
      #   return redirect(request.POST.get('next'))
      # else:
      #   return redirect("blog-home")
  else:
    form = AuthenticationForm()
  return render(request, 'users/login.html', { "form" : form })

def logout_view(request):
  if(request.method == "POST"):
    logout(request)
    return render(request, "users/logout.html")
  
@login_required
def profile_view(request):
  if request.method == "POST":
    userForm = UserUpdate(request.POST, instance=request.user)
    profileForm = ProfileUpdate(request.POST, 
                                request.FILES,
                                instance=request.user.profile)
    if userForm.is_valid() and profileForm.is_valid():
      # username = userForm.cleaned_data.get('username')
      userForm.save()
      profileForm.save()
      messages.success(request, f'Profile has been updated!')
      return redirect('profile')
    
  else:
    userForm = UserUpdate(instance=request.user)
    profileForm = ProfileUpdate(instance=request.user.profile)
  context = {
    'userForm': userForm,
    'profileForm': profileForm
  }
  return render(request, 'users/profile.html', context)
  


# message.debug
# message.success
# message.error
# message.info