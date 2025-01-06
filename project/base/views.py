from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import WorkItem

class Login(LoginView):
    template_name = 'base/login.html'
    field = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('pendings')

class CreateAccountPage(FormView):
    template_name = 'base/create_account.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('pendings')
    
    def form_valid(self, form):
        usuario = form.save()
        if usuario is not None:
            login(self.request, usuario)
        return super(CreateAccountPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('pendings')
        return super().get(*args, **kwargs)

class ListPending(LoginRequiredMixin, ListView):
    model = WorkItem
    context_object_name = 'work_items'
    template_name = 'base/work_items_list.html'
    
    def get_context_data(self, **kwarg):
        context = super().get_context_data(**kwarg)
        context['work_items'] = context['work_items'].filter(user= self.request.user)
        context['count'] = context['work_items'].filter(completed=False).count()
        return context
    
class DetailWorkItem(LoginRequiredMixin, DetailView):
    model = WorkItem
    context_object_name = 'work_item'
    template_name = 'base/work_item_detail.html'
    
class CreateWorkItem(LoginRequiredMixin, CreateView):
    model = WorkItem
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('pendings')
    template_name = 'base/work_item_form.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateWorkItem, self).form_valid(form)
    
class UpdateWorkItem(LoginRequiredMixin, UpdateView):
    model = WorkItem
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('pendings')
    template_name = 'base/work_item_form.html'
    
class DeleteWorkItem(LoginRequiredMixin, DeleteView):
    model = WorkItem
    context_object_name = 'work_item'
    success_url = reverse_lazy('pendings')
    template_name = 'base/work_item_confirm.html'