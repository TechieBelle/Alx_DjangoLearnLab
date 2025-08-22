from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import RegisterForm, UserUpdateForm, ProfileForm

class RegisterView(FormView):
    template_name = "accounts/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("profile")

    def form_valid(self, form):
        user = form.save()          # creates the User (Profile is auto-created by signal)
        login(self.request, user)   # log them in immediately
        return super().form_valid(form)

@login_required
def profile_view(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)

    return render(request, "accounts/profile.html", {"u_form": u_form, "p_form": p_form})

