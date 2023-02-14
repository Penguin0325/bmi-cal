from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import BmiModel
from .forms import BmiFormClass
from django.shortcuts import redirect
from django.urls import reverse
from urllib.parse import urlencode

@csrf_exempt
def bmiIndexView(request):
    return render(request, "bmi/index.html")

@csrf_exempt
def bmiCreateView(request):
    template_name="bmi/index.html"
    form = BmiFormClass()

    ctx={}
    ctx["form"]=form

    if request.POST:
        user = request.POST["user"]
        age = request.POST["age"]
        weight = request.POST["weight"]
        height = request.POST["height"]
        print(user)
        print(age)
        print(weight)
        print(height)
        obj = BmiModel(user=user, age=age, weight=weight, height=height)
        obj.save()

        redirect_url = reverse("bmi-home")
        parameter = urlencode({'user':user})

        url = f'{redirect_url}?{parameter}'

        return redirect(url)
    
    return render(request, template_name, ctx)

@csrf_exempt
def bmiHomeView(request):
    template_name="bmi/home.html"
    user = request.GET['user']
    # print(user)

    q = BmiModel.objects.get(user=user)
    
    bmi = q.weight/((q.height/100)*(q.height/100))
    standard = ((q.height/100)*(q.height/100))*22
    model = ((q.height/100)*(q.height/100))*18
    if standard > q.weight:
        diff = standard - q.weight
    elif standard <q.weight:
        diff = q.weight - standard
    elif standard == q.weight:
        diff = 0

    if model<q.weight:
        diff_model = q.weight-model

    
    ctx = {
        "bmi" : bmi,
        "standard" : standard,
        "diff" : diff,
        "model" : model,
        "diff_model" : diff_model
    }

    return render(request, template_name, ctx)