from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Task, UserProfile
from django.contrib.auth.decorators import login_required

@login_required
def task_list(request):
    if request.user.userprofile.is_admin:
        return redirect('admin:index')
    else:
        tasks = Task.objects.filter(user=request.user)
        search_query = request.GET.get('search-area')  # Updated to use 'search-area'
        if search_query:
            tasks = tasks.filter(title__icontains=search_query)  # Filter tasks based on the search query
        paginator = Paginator(tasks, 10)  # Display 10 tasks per page

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'page_obj': page_obj,
            'search_query': search_query,  # Pass search query to the template
        }
        return render(request, 'todo/tasklist.html', context)

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name ='todo/tasklist.html'
    paginate_by = 10  # Display 10 tasks per page

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        search_query = self.request.GET.get('search-area') or ''  # Updated to use 'search-area'
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = context['tasks'].filter(complete=False).count()
        context['search_input'] = self.request.GET.get('search-area') or ''  # Updated to use 'search-area'
        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todo/taskdetail.html'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'todo/taskcrud.html'
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('task')

    def form_valid(self, form):
        if self.request.user.userprofile.is_admin:
            return redirect('admin:index')
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'todo/taskcrud.html'
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('task')

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'todo/delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('task')

class CustomLoginView(LoginView):
    template_name = 'todo/login.html'
    fields = "__all__"
    redirect_authenticated_user = False

    def get_success_url(self):
        return reverse_lazy('task')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.userprofile.is_blocked:
                messages.error(self.request, 'Tài khoản của bạn đã bị khóa.')
                return self.form_invalid(form)
            login(self.request, user)
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

class RegisterPage(FormView):
    template_name = 'todo/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('task')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('task')
        return super(RegisterPage, self).get(*args, *kwargs)

class TaskDeleteMultiple(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        task_ids = request.POST.getlist('task_ids')
        if task_ids:
            tasks = Task.objects.filter(id__in=task_ids, user=request.user)
            tasks.delete()
            return HttpResponseRedirect(reverse_lazy('task'))
        return JsonResponse({'message': 'Không có nhiệm vụ nào được chọn'}, status=400)
