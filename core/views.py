from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'
    
    
class ProfilePageView(TemplateView):
    template_name = 'profile.html'
    
    
class MeekPageView(TemplateView):
    template_name = 'meek.html'


