from django.views import View
from django.shortcuts import redirect, get_object_or_404
from ..models import Todo


class TodoUpdateView(View):
    def post(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)
        status = request.POST.get("status")
        if status in ["PENDING", "IN_PROGRESS", "COMPLETED"]:
            todo.status = status
            todo.save()
        return redirect('todo_list')
