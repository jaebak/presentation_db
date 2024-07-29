from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Presentation
from .forms import PresentationForm
from .tables import PresentationTable
from .filters import PresentationFilter
import os
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from django.conf import settings
from urllib.parse import urlparse
import requests
import browser_cookie3

def save_pdf_url_to_file(pdf_url_link):
    file_name = os.path.basename(urlparse(pdf_url_link).path)
    if not file_name.endswith('.pdf'):
        file_name += '.pdf'
    
    file_dir = os.path.join(settings.MEDIA_ROOT, 'pdf_files')
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)

    file_path = os.path.join(file_dir, file_name)
    file_base, file_extension = os.path.splitext(file_path)
    counter = 1

    while os.path.exists(file_path):
        file_path = f"{file_base}_{counter}{file_extension}"
        counter += 1

    cookiejar = browser_cookie3.firefox(domain_name='cern.ch')
    response = requests.get(pdf_url_link, cookies=cookiejar, verify=False)
    with open(file_path, 'wb') as file:
        file.write(response.content)
    return file_path

class PresentationListView(SingleTableMixin, FilterView):
    model = Presentation
    table_class = PresentationTable
    template_name = 'jpresent/presentation_list.html'
    filterset_class = PresentationFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-date')  # Orders by date descending


class PresentationCreateView(CreateView):
    model = Presentation
    form_class = PresentationForm
    template_name = 'jpresent/presentation_form.html'
    success_url = reverse_lazy('presentation_list')

    def form_valid(self, form):
        # Save url link to local file
        pdf_url_link = form.cleaned_data.get('pdf_url_link')
        save_pdf_from_url = form.cleaned_data.get('save_pdf_from_url')
        if pdf_url_link and save_pdf_from_url:
            file_path = save_pdf_url_to_file(pdf_url_link)
            form.instance.pdf_file = os.path.relpath(file_path, settings.MEDIA_ROOT)
        return super().form_valid(form)

class PresentationUpdateView(UpdateView):
    model = Presentation
    form_class = PresentationForm
    template_name = 'jpresent/presentation_form.html'
    success_url = reverse_lazy('presentation_list')

    def form_valid(self, form):
        presentation = self.get_object()
        save_pdf_from_url = form.cleaned_data.get('save_pdf_from_url')
        if 'pdf_url_link' in form.changed_data or 'pdf_file' in form.changed_data or save_pdf_from_url:
            # Remove old file
            if presentation.pdf_file:
                old_file_path = presentation.pdf_file.path
                if os.path.isfile(old_file_path):
                    os.remove(old_file_path)

            # Save url link to local file
            pdf_url_link = form.cleaned_data.get('pdf_url_link')
            if pdf_url_link and save_pdf_from_url:
                file_path = save_pdf_url_to_file(pdf_url_link)
                form.instance.pdf_file = os.path.relpath(file_path, settings.MEDIA_ROOT)
        return super().form_valid(form)

class PresentationDeleteView(DeleteView):
    model = Presentation
    template_name = 'jpresent/presentation_confirm_delete.html'
    success_url = reverse_lazy('presentation_list')

    def form_valid(self, form):
        if self.object.pdf_file:
            file_path = self.object.pdf_file.path
            if os.path.isfile(file_path):
                os.remove(file_path)
        return super().form_valid(form)

