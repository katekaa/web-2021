from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms
from .models import *
from datetime import datetime

def index(request):
    return render(request, 'index.html')

def report(request):
    libraries = Library.objects.all()
    params = {'libraries': libraries, 'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    return render(request, 'report.html', params)

def lang_list(request):
    languages = Language.objects.all().values()
    params = {'entity': 'Language', 'objects': languages}
    return render(request, 'list.html', params)

def library_list(request):
    libraries = Library.objects.all().values()
    params = {'entity': 'Library', 'objects': libraries}
    return render(request, 'list.html', params)

class LanguageCreate(CreateView):
    model = Language
    fields = ['name', 'extension', 'ide']
    success_url = '/lang'
    template_name = 'lang_form.html'

class LanguageUpdate(UpdateView):
    model = Language
    fields = ['name', 'extension', 'ide']
    pk_url_kwarg = 'id'
    success_url = '/lang'
    template_name = 'lang_form.html'

class LanguageDelete(DeleteView):
    model = Language
    pk_url_kwarg = 'id'
    success_url = '/lang'
    template_name = 'lang_delete_form.html'

class LibraryCreate(CreateView):
    model = Library
    fields = ['name','lang']
    success_url = '/library'
    template_name = 'library_form.html'

    def get_context_data(self, **kwargs):
        context = super(LibraryCreate, self).get_context_data(**kwargs)
        context['form'].fields['lang'] = forms.ModelChoiceField(queryset=Language.objects.all(), empty_label=None, label='Языки')
        return context

class LibraryUpdate(UpdateView):
    model = Library
    fields = ['name', 'lang']
    pk_url_kwarg = 'id'
    success_url = '/library'
    template_name = 'library_form.html'

    def get_context_data(self, **kwargs):
        context = super(LibraryUpdate, self).get_context_data(**kwargs)
        context['form'].fields['lang'] = forms.ModelChoiceField(queryset=Language.objects.all(),
                                                                    empty_label=None, label='Language')
        return context

class LibraryDelete(DeleteView):
    model = Library
    pk_url_kwarg = 'id'
    success_url = '/library'
    template_name = 'library_delete_form.html'