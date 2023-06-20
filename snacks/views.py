from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView,CreateView, UpdateView, DeleteView
from .models import Snack
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = "home.html"

class SnackListView(ListView):
    template_name = "snack_list.html"
    model = Snack
    context_object_name = "snacks"


class SnackDetailView(DetailView):
    template_name = "snack_detail.html"
    model = Snack

class SnackCreateView (CreateView):
    template_name='snack_create.html'
    model=Snack
    fields= ['name', 'purchaser', 'desc']

class SnackUpdateView (UpdateView):
    template_name='snack_update.html'
    model=Snack
    fields="__all__"
    success_url=reverse_lazy('snack_list')

class SnackDeleteView(DeleteView):
    template_name='snack_delete.html'
    model=Snack
    success_url=reverse_lazy('snack_list')

