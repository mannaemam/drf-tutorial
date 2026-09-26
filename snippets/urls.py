from django.urls import path

import snippets
from snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<slug:slug>', views.snippet_detail),
]