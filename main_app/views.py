from django.shortcuts import render, redirect
from .forms import WidgetForm

# Models
from .models import Widget


# Create your views here.
    
def index(request):
    widget_form = WidgetForm()
    widgets = Widget.objects.all()
    return render(request, 'index.html', {'widget_form': widget_form, 'widgets': widgets})

def add_widget(request):
    form = WidgetForm(request.POST)
    if form.is_valid():
        new_widget = form.save()
    return redirect('index')