from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View


class SignupView(View):
    template_name = 'registration/signup.html'

    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # or reverse('login')
        return render(request, self.template_name, {'form': form})
