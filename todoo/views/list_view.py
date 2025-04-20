from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from ..models import Todo


class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = 'todo_list.html'
    context_object_name = 'todos'

    def get_queryset(self):
        """Only show current user's todos"""
        return Todo.objects.filter(user=self.request.user).order_by(
            '-created_at')

    def get_context_data(self, **kwargs):
        """Add photo_url to context if needed"""
        context = super().get_context_data(**kwargs)
        context[
            'cloudinary_cloud_name'] = 'todoo'  # For JS upload widget
        return context
