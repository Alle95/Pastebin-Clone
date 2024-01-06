from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import text
from .forms import textForm

def show_text(request, text_id):
    textList = text.objects.get(pk=text_id)
    return render(request, 'show_text.html', {'textList': textList})

def home_page(request):
    return render(request, 'home.html')

def add_text(request):
    form = textForm
    if request.method == 'POST':
        form = textForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('history'))
    return render(request, 'addText.html', {'form': form})

def history(request):
    pastebinList = text.objects.all()
    return render(request, 'history.html', {'pastebinList': pastebinList})
