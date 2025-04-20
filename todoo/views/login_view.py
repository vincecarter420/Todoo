from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


class LoginView(View):
    template_name = 'registration/login.html'
    form_class = AuthenticationForm
    redirect_authenticated_user = True

    def get(self, request):
        if self.redirect_authenticated_user and request.user.is_authenticated:
            return redirect('todo_list')
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('todo_list')
        return render(request, self.template_name, {'form': form})