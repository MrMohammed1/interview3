from django.urls import path
from . import views

# app_name = 'people'

urlpatterns = [
    path('', views.person_list, name='person_list'),  # List all people
    path('create/', views.PersonCreateView.as_view(), name='person_create'),  # Create a person
    path('update/<int:pk>/', views.PersonUpdateView.as_view(), name='person_update'),  # Update a person
    path('delete/<int:pk>/', views.PersonDeleteView.as_view(), name='person_delete'),  # Delete a person
    path('detail/<int:pk>/', views.PersonDetailView.as_view(), name='person_detail'),  # Detail view of a person
]
