import django_tables2 as tables
from .models import Presentation

class PresentationTable(tables.Table):
    edit = tables.TemplateColumn(
        template_code='<a href="{% url \'presentation_edit\' record.pk %}">Edit</a>',
        verbose_name='Edit',
        orderable=False,
        attrs={"td": {"class": "text-center"}}
    )
    delete = tables.TemplateColumn(
        template_code='<a href="{% url \'presentation_delete\' record.pk %}">Delete</a>',
        verbose_name='Delete',
        orderable=False,
        attrs={"td": {"class": "text-center"}}
    )

    pdf_url_link = tables.TemplateColumn(
        template_code='{% if record.pdf_url_link %}<a href="{{ record.pdf_url_link }}">link</a>{% else %}No link{% endif %}',
        verbose_name="PDF URL Link",
        attrs={"td": {"class": "text-center"}}
    )
    pdf_file = tables.TemplateColumn(
        template_code='{% if record.pdf_file %}<a href="{{ record.pdf_file.url }}">local link</a>{% else %}No file{% endif %}',
        verbose_name="PDF File",
        attrs={"td": {"class": "text-center"}}
    )

    class Meta:
        model = Presentation
        template_name = "django_tables2/bootstrap4.html"
        fields = ("date", "tag", "title", "author", "notes", "pdf_url_link", "pdf_file", "edit", "delete")
        attrs = {"class": "table table-striped table-bordered"}

