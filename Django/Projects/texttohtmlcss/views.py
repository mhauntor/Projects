from django.shortcuts import render
#from .models import Generator
from .forms import GeneratorForm


def textToHtml(request):
    form = GeneratorForm()
    return render(request, 'htmlgen/text2html.html', {'form': form})
