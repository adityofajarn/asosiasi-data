from django.shortcuts import render
from .forms import Result
from .asosiasi import Association

# Create your views here.
def home(response):
    form = Result()
    return render(response, 'main/home.html', {"form" : form})

def result(response):
    if response.method == "POST":
        form = Result(response.POST)

        if form.is_valid():
            support = float(form.cleaned_data['a'])
            confidence = float(form.cleaned_data['b'])
            count = Association(support, confidence)

            return render(response, 'main/result.html', {"result" : count})

    else:
        form = Result()

    return render(response, 'main/result.html', {"form" : form})
