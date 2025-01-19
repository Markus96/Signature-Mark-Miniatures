# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from .models import Product, User
from .forms import RegistrationForm, LoginForm

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(email=form.cleaned_data['email']).first()
            if user and check_password(form.cleaned_data['password'], user.password):
                request.session['user_id'] = str(user.id)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def products(request):
    products_list = Product.objects.all()
    return render(request, 'products.html', {'products': products_list})

def add_products(request):
    # Sample product data
    products = [
        { "name": "Dragon Miniature", "price": 15.99, "description": "A detailed dragon miniature." },
        { "name": "Knight Miniature", "price": 12.99, "description": "A brave knight miniature." },
        { "name": "Castle Miniature", "price": 20.99, "description": "A grand castle miniature." },
        { "name": "Elf Archer Miniature", "price": 10.99, "description": "An elf archer with a longbow." },
        { "name": "Orc Warrior Miniature", "price": 14.99, "description": "A fierce orc warrior miniature." },
        { "name": "Wizard Miniature", "price": 13.99, "description": "A wizard with a staff and spellbook." },
        { "name": "Goblin Miniature", "price": 9.99, "description": "A mischievous goblin miniature." },
        { "name": "Dwarf Warrior Miniature", "price": 11.99, "description": "A stout dwarf warrior miniature." },
        { "name": "Necromancer Miniature", "price": 16.99, "description": "A dark necromancer with a skull staff." },
        { "name": "Giant Miniature", "price": 22.99, "description": "A towering giant miniature." }
    ]
    
    # Check if products are already in the collection
    if Product.objects.count() == 0:
        Product.objects.bulk_create([Product(**prod) for prod in products])
        return HttpResponse("Products added successfully!")
    else:
        return HttpResponse("Products already exist in the collection.")