from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Models
from .models import Widget
# from .forms import WidgetForm

# Create your views here.

class WidgetCreate(CreateView):
    model = Widget
    fields = '__all__'
    success_url = '/'
    
def index(request):
    return render(request, 'index.html')
