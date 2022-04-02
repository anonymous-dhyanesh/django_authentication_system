from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    return render(request, "index.html") 

def loginUser(request):
    if request.method == "POST":
        # Fetching username from the request
        username = request.POST.get('username')
        # Fetching pasdsword from the request
        password = request.POST.get('password')

        # Autenticatig user , if user entered correct deatils 
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "login.html", {
                "message" : "invalid username or password"
            })
    
    return render(request, "login.html")

def logoutUser(request):
    logout(request)
    return render(request, "login.html",{
        "message" : "Logged Out"
    })

