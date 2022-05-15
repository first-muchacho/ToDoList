from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'task_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_list'] = context['task_list'].filter(user=self.request.user)
        context['count'] = context['task_list'].filter(completed=False).count()
        search = self.request.GET.get('search_form') or ''
        if search:
            context['task_list'] = context['task_list'].filter(title__icontains=search)
        context['search'] = search
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'core/task.html'


class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description']
    success_url = reverse_lazy('task_list')
    template_name = 'core/create_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTask, self).form_valid(form)


class UpdateTask(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('task_list')
    template_name = 'core/create_form.html'


class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task_list')
    template_name = 'core/delete_task.html'
