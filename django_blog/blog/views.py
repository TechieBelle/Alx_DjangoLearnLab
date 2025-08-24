from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import RegisterForm, UserUpdateForm, ProfileForm
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView 
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import PostForm


class IndexView(TemplateView):
    template_name = 'blog/index.html'   


class RegisterView(CreateView):
    template_name = "blog/register.html"
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

    return render(request, "blog/profile.html", {"u_form": u_form, "p_form": p_form})


# Imlementing CRUD perations for BlogPost model using class-based views
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']  # show newest first

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    form_class = PostForm
    success_url = reverse_lazy('post_list')

    def form_valid(self, form): 
        form.instance.author = self.request.user  # Set the author to the logged-in user
        return super().form_valid(form)          



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    form_class = PostForm
    success_url = reverse_lazy('post_list')    

    def form_valid(self, form):
        # ensure author is still the logged-in user
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# Delete a post (only the author can delete)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')                                                                   
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only allow the author to delete the post                   
     



