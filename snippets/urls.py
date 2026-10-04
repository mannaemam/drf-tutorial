from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views


from snippets.views import UserViewSet

user_list = UserViewSet.as_view({'get': 'list'})
user_detail = UserViewSet.as_view({'get': 'retrieve'})

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<slug:slug>/', views.SnippetDetail.as_view()),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/',user_detail, name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)