from msilib.schema import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from departments.models import Department


class DepartmentListView(LoginRequiredMixin, ListView):
    model = Department
    template_name = 'departments.html'
    login_url = 'login'


class DepartmentDetailView(LoginRequiredMixin, DetailView):
    model = Department
    template_name = 'departments_detail.html'
    fields = ['name', 'description', 'structure', 'work_at_events', 'internal_events', 'faq', 'useful_sources']
    login_url = 'login'


class DepartmentCreateView(LoginRequiredMixin, CreateView):
    model = Department
    template_name = ''
    fields = ['name', 'description', 'structure', 'work_at_events', 'internal_events', 'faq', 'useful_sources']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)


class DepartmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Department
    template_name = ''
    fields = ['name', 'description', 'structure', 'work_at_events', 'internal_events', 'faq', 'useful_sources']
    login_url = 'login'


class DepartmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Department
    template_name = ''
    fields = ['name', 'description', 'structure', 'work_at_events', 'internal_events', 'faq', 'useful_sources']
    login_url = 'login'















# Create your views here.
