from django.shortcuts import render
from django.views.generic import TemplateView


class AuthorPageView(TemplateView):
   template_name = 'pages/author.html'
