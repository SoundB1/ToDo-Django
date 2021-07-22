from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .forms import ToDoForm
from .models import Task

class HomeView(generic.ListView):
    template_name = "index.html"
    model = Task

class TaskDeleteView(generic.View):
    
    def get(self, request, *args, **kwargs):
        
        tasks = get_object_or_404(Task, id=kwargs['pk'])
        tasks.delete()
        return redirect('home')


class TaskCompleteView(generic.View):    
    def get(self, request, *args, **kwargs):
        
        tasks = get_object_or_404(Task, id=kwargs['pk'])
        tasks.complete = True
        tasks.save()
        return redirect('home')

class TaskEditView(generic.View):
    template_name = 'edit.html'
    form_class = ToDoForm

    def get(self, request, *args, **kwargs):
        
        tasks = get_object_or_404(Task, id=kwargs['pk'])
        if tasks.complete:
            return redirect('home')
        else:
            return render(request, self.template_name, {'tasks': tasks })

    def post(self, request, *args, **kwargs):
        
        form = self.form_class(request.POST)
        if form.is_valid():
            tasks = get_object_or_404(Task, id=kwargs['pk'])
            
            infForm = form.cleaned_data
            tasks.task_name = infForm['task_name']
            tasks.description = infForm['description']
            tasks.save()
            return redirect('home')        

class ToDoView(generic.View):
    template_name = 'todo.html'
    form_class = ToDoForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'success': False })

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            infForm = form.cleaned_data

            ToDoData__ = Task(
                task_name=infForm['task_name'],
                description=infForm['description'])
            ToDoData__.save()

        return render(request, self.template_name, {'success': True} )