from .models import User
from django.views.generic import TemplateView, View, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy


class Index(TemplateView):
    template_name = 'blog/index.html'


class LoginView(LoginView):
    template_name = 'blog/registration/login.html'
    redirect_authenticated_user = True


class LogoutView(LogoutView):
    template_name = 'blog/registration/logout.html'
    redirect_authenticated_user = True



class RegisterView(CreateView):
        template_name = 'blog/registration/register.html'
        form_class = UserCreationForm
        success_url = reverse_lazy("login")
        def form_valid(self, form):
             user = form.save()
             login(self.request, user)
             return super().form_valid(form)    
        

class ProfileView(View):
   template_name = 'blog/profile.html'
    # def get_success_url(self):
    #     return self.request.GET.get('next', 'home')

# def register_view(request):   
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = User.objects.create_user(username=username, password=password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = RegisterForm()
#         return render(request, 'registration/register.html', {'form': form})

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             error_message = 'Invalid credentials!'
#     return render(request, 'registration/login.html',{'error_message': error_message})



# def logout_view(request):
#     if request.method == 'POST':
#         logout(request)
#         return redirect('login')
#     else:
#         return redirect('home')




