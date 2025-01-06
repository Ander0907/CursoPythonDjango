from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import WorkItem

class ListPending(ListView):
    model = WorkItem
    context_object_name = 'work_items'
    template_name = 'base/work_items_list.html'
    
class DetailWorkItem(DetailView):
    model = WorkItem
    context_object_name = 'work_item'
    template_name = 'base/work_item_detail.html'
    
class CreateWorkItem(CreateView):
    model = WorkItem
    fields = '__all__'
    success_url = reverse_lazy('pendings')
    template_name = 'base/work_item_form.html'
    
class UpdateWorkItem(UpdateView):
    model = WorkItem
    fields = '__all__'
    success_url = reverse_lazy('pendings')
    template_name = 'base/work_item_form.html'
    
class DeleteWorkItem(DeleteView):
    model = WorkItem
    context_object_name = 'work_item'
    success_url = reverse_lazy('pendings')
    template_name = 'base/work_item_confirm.html'