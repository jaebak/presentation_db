import django_filters
from .models import Presentation
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class PresentationFilter(django_filters.FilterSet):
    class Meta:
        model = Presentation
        fields = ['date', 'tag', 'title', 'author']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form.helper = FormHelper()
        self.form.helper.form_method = 'GET'
        self.form.helper.add_input(Submit('submit', 'Filter'))
