from .memoviews import *
from .personviews import *
from .memopersonviews import *
from django.shortcuts import render
from django.views.generic import TemplateView
#If facing problems: Use this : https://stackoverflow.com/questions/12784835/django-no-such-table
def home(req):
    return render(req, 'index.html')

# Add the two views we have been talking about  all this time :)
class HomePageView(TemplateView):
    template_name = "index.html"