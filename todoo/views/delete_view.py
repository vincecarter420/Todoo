from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from ..models import Todo


class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo
    template_name = 'todo_confirm_delete.html'
    success_url = reverse_lazy('todo_list')

    def get_queryset(self):
        """Only allow deleting own todos"""
        return Todo.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        """Optional: Delete Cloudinary photo when todo is deleted"""
        todo = self.get_object()
        if todo.photo:
            todo.photo.delete()  # Deletes from Cloudinary
        return super().delete(request, *args, **kwargs)