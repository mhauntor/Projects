from django import forms
from .models import Generator
from ckeditor.widgets import CKEditorWidget


class GeneratorForm(forms.ModelForm):
    doctext = forms.CharField(widget=CKEditorWidget(), label="Text Editor")
    class Meta:
        model = Generator
        fields = ('doctext',)
