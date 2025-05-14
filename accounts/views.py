from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import SignUpForm, LoginForm, UserUpdateForm, ProfileUpdateForm, CustomPasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from blog.models import Post
from django.contrib import messages


class AuthView(View):
    def get(self, request):
        return render(request, 'accounts/auth.html', {
            'signup_form': SignUpForm(),
            'login_form': LoginForm()
        })

    def post(self, request):
        if 'signup' in request.POST:
            signup_form = SignUpForm(request.POST)
            if signup_form.is_valid():
                user = signup_form.save(commit=False)
                user.set_password(signup_form.cleaned_data['password'])
                user.save()
                login(request, user)
                return redirect('/')
        elif 'login' in request.POST:
            login_form = LoginForm(data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect('/')
        return render(request, 'accounts/auth.html', {
            'signup_form': SignUpForm(request.POST),
            'login_form': LoginForm(request.POST)
        })
    
    def form_valid(self, request):
        messages.success(self.request, "Login Successful.")
        return super().form_valid(request)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('accounts:auth')



class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['liked_posts'] = Post.objects.filter(likes=user).order_by('-date_published')
        context['bookmarked_posts'] = Post.objects.filter(bookmarks=user).order_by('-date_published')
        context['u_form'] = UserUpdateForm(instance=user)
        context['p_form'] = ProfileUpdateForm(instance=user.profile)

        return context

    def post(self, request, *args, **kwargs):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('accounts:dashboard')

        # fallback with errors and re-populating all context
        context = self.get_context_data()
        context['u_form'] = u_form
        context['p_form'] = p_form
        return self.render_to_response(context)



class ChangePasswordView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('accounts:dashboard')

    def form_valid(self, form):
        messages.success(self.request, "Your password was successfully changed.")
        return super().form_valid(form)