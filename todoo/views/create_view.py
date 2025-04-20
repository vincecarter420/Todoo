from django.views.generic import CreateView

from ..forms import TodoForm
from ..models import Todo


class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'create_todo.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)