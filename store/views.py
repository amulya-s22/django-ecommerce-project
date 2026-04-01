from django.shortcuts import render,redirect
from .models import Product
# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def cart(request):
    cart = request.session.get('cart', [])
    products = Product.objects.filter(id__in=cart)
    return render(request, 'cart.html', {'products': products})

def add_to_cart(request, product_id):
    cart = request.session.get('cart', [])

    cart.append(product_id)

    request.session['cart'] = cart
    request.session.modified = True   

    return redirect('home')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', [])

    if product_id in cart:
        cart.remove(product_id)

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart')

def checkout(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')

        # Clear cart after order
        request.session['cart'] = []

        return render(request, 'success.html', {'name': name})

    return render(request, 'checkout.html')

