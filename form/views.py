from django.shortcuts import render
from django.http import HttpResponse
from ..app1.forms import Register
from app1.models import RegisterModel

def register(request):
    if request.method == "POST" and request.FILES:
        form = Register(request.POST,request.FILES)
        if form.is_valid():
            print("firstname:", form.cleaned_data['firstname'])
            print("lastname:", form.cleaned_data['lastname'])
            print("age: ", form.cleaned_data['age'])
            print("dob: ", form.cleaned_data['dob'])
            print("gender: ", form.cleaned_data['gender'])
            print("email: ", form.cleaned_data['email'])
            print("phone: ", form.cleaned_data['phone'])
            print("username: ", form.cleaned_data['username'])
            print("password: ", form.cleaned_data['password'])
            print("confirmPassword: ", form.cleaned_data['confirmPassword'])
            create = RegisterModel.objects.create(firstname=form.cleaned_data['firstname'],
                                                  lastname=form.cleaned_data['lastname'],
                                                  age=form.cleaned_data['age'],
                                                  dob=form.cleaned_data['dob'],
                                                  gender=form.cleaned_data['gender'],
                                                  email=form.cleaned_data['email'],
                                                  phone=form.cleaned_data['phone'],
                                                  username=form.cleaned_data['username'],
                                                  password=form.cleaned_data['password'],
                                                  file=form.cleaned_data['file'])

            create.save()
            print("Data's Are Stored inside the Database")
    else:
        form = Register()
    return render(request, "base.html", {"form": form, "VE": ValueError})


def login(request):
    form = Register()
    if request.method == "POST":
        form = Register(request.POST, request.FILES)
        user = request.POST['username']
        passw = request.POST['password']
        print(user, passw)
        res = RegisterModel.objects.all()
        for i in res:
            if i.username == user:
                if i.password == passw:
                    return render(request, 'home.html', {'i': i})
                else:
                    return HttpResponse("Incorrect Password")

    return render(request, 'login.html', {'form': form})
