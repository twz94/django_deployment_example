from django.shortcuts import render
from myapp import forms

# Create your views here.

def index(request):
    return render (request, 'myapp/index.html')


def helpview(request):
    return render(request, 'myapp/helpview.html')


def form_name_view(request):
    form = forms.Form_name()


    if request.method == 'POST':
        form=forms.Form_name(request.POST)

        if form.is_valid():
            # DO SOMETHING CODE
            print('VALIDATION SUCCESS!')    
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT: "+form.cleaned_data['text'])




    return render(request, 'myapp/form_name.html', {'form': form})
