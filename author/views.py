from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from .models import Author
class AuthorPageView(TemplateView):
   template_name = 'pages/author.html'


class AuthorListView(ListView):
    model = Author
    paginate_by = 10
