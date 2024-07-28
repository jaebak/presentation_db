from django.urls import path
from .views import PresentationListView, PresentationCreateView, PresentationUpdateView, PresentationDeleteView

urlpatterns = [
    path('', PresentationListView.as_view(), name='presentation_list'),
    path('create/', PresentationCreateView.as_view(), name='presentation_create'),
    path('edit/<int:pk>/', PresentationUpdateView.as_view(), name='presentation_edit'),
    path('delete/<int:pk>/', PresentationDeleteView.as_view(), name='presentation_delete'),
]

