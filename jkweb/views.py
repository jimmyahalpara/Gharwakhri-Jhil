from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from accounts.models import registery
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def my_view(request):
    r1 = random.randint(0, 9)
    r2 = random.randint(0, 9)
    r3 = random.randint(0, 9)
    r4 = random.randint(0, 9)
    context = {
        'r1': r1,
        'r2': r2,
        'r3': r3,
        'r4': r4,
    }
    return render(request, 'page-login.html', context)

def home(request):
    
    return render(request, 'index-3.html')

def signup(request):
    if request.method == 'POST':
        # create new user object 
        user = User.objects.create_user(
            username=request.POST.get('username'),
            password=request.POST.get('password1'),
            email=request.POST.get('email'),
        )
        # save user object
        user.save()

        phone=request.POST.get('phoneno')
        city=request.POST.get('city')
        question=request.POST.get('question')
        answer=request.POST.get('answer')
        role=request.POST.get('role')
        terms=request.POST.get('terms')
        if  terms=='agree':
            term=True
        else:
            term=False
            
        sv = registery(phoneno=phone,city=city,question=question,answer=answer,role=role,terms=term, user=user)
        sv.save()
        # login user
        login(request, user)
        return redirect('home')
        # login(request, sv)
    else:
        
        return render(request, 'page-register.html')

def loginin(request):
    # clear current session
    request.session.flush()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print ("Invalid login credentials")
            context = {'error': 'Invalid login credentials'}
            return render(request, 'page-login.html', context)
    else:
        return render(request, 'page-login.html')
def logout(request):
    # clear current session
    request.session.flush()
    return redirect('home')

def pgregister(request):
    return render(request, 'register.html')

def pgabout(request):
    return render(request, 'page-about.html')


def pgaccount(request):
    return render(request, 'page-account.html')

def pgcontact(request):
    return render(request, 'page-contact.html')



def pgpvtpolicy(request):
    return render(request, 'page-privacy-policy.html')

def purchaseguide(request):
    return render(request, 'page-purchase-guide.html')

def shopcart(request):
    return render(request, 'shop-cart.html')

def shopcompare(request):
    return render(request, 'shop-compare.html')


def shopinvoice(request):
    return render(request, 'shop-invoice.html')



def shopwish(request):
    return render(request, 'shop-wishlist.html')
