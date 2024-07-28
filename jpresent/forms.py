from django import forms
from .models import Presentation
import os
from urllib.parse import urlparse
import requests
from django.conf import settings
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class PresentationForm(forms.ModelForm):
    save_pdf_from_url = forms.BooleanField(initial=True, required=False)

    class Meta:
        model = Presentation
        fields = ['date', 'title', 'author', 'notes', 'pdf_url_link', 'pdf_file', 'tag']

    def __init__(self, *args, **kwargs):
        super(PresentationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

