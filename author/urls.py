from django.urls import path

from .views import AuthorPageView

urlpatterns = [
   path('', AuthorPageView.as_view(), name='author'),

]