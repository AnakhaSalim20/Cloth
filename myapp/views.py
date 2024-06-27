from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib import auth,messages
from django.contrib.auth import login
from django.contrib.auth import logout
from .forms import customerreg, userreg
from .models import CartItem
from django.shortcuts import render, get_object_or_404
from .models import  Productz
#from .models import Paymentz
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import customerreg, userreg

def signup(request):
    if request.method == 'POST':
        form1 = userreg(request.POST)
        form2 = customerreg(request.POST)
        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            user.is_customer = True
            user.save()
            customer = form2.save(commit=False)
            customer.user = user
            customer.save()
            return redirect('loginpage')
    else:
        form1 = userreg()
        form2 = customerreg()

    return render(request, 'signup.html', {'form1': form1, 'form2': form2})


def home(request):
    return render(request,'home.html') 

def about(request):
    return render(request,'aboutus.html')

def contact(request):
    return render(request,'contact.html')

def blog(request):
    return render(request,'blog.html')

def faq(request):
    return render(request,'faq.html')

def terms(request):
    return render(request,'terms.html')

def privacy_policy(request):
    return render(request, 'policy.html')

def log(request):
    return render(request,'logbook.html')


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('text')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_staff:
                auth.login(request, user)
                return redirect('admin')  
            elif user.is_customer:
                auth.login(request, user)
                return redirect('bag') 
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')


def admin(request):
    return render(request,'adminindex.html')

def logout_request(request):
    logout(request)
    messages.info(request,"Logged Out Successfully")
    return redirect("home")


#def view_cart(request):
 #   cart_items = CartItem.objects.filter(user=request.user)
  #  total_price = sum(item.name.price * item.quantity for item in cart_items)
   # return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


#def add_to_cart(request, product_id):
 #   product = Product.objects.get(id=product_id)
  #  cart_item, created = CartItem.objects.get_or_create(product=product, 
   #                                                    user=request.user)
    #cart_item.quantity += 1
    #cart_item.save()
    #return redirect('view_cart')
 
 

#@login_required
#def view_cart(request):
 #   cart_items = CartItem.objects.filter(user=request.user)
  #  print(cart_items)  # Check what items are being fetched
   # total_price = sum(item.total_price for item in cart_items)
   # print(total_price)  # Check total price calculation
   # return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


#def checkout(request):
    # Your checkout logic here
 #   return render(request, 'checkout.html')

def checkout(request):
    return render(request,'home.html')

#def men(request):
 #   data = Product.objects.filter(category='Men')
  #  return render(request, 'shop.html', {'data': data, 'category': 'Men'})

#def women(request):
 #   data = Product.objects.filter(category='Women')
  #  return render(request, 'shop.html', {'data': data, 'category': 'Women'})

#def shop(request):
 #   data=Product.objects.all()
  #  return render(request,'shop.html',{'data':data})
#def men(request):
 #   men_count = Product.objects.filter(category='Men').count()
  #  data = Product.objects.filter(category='Men')
   # return render(request, 'shop.html', {'data': data, 'category': 'Men', 'product_count': men_count})

#def women(request):
 #   women_count = Product.objects.filter(category='Women').count()
  #  data = Product.objects.filter(category='Women')
   # return render(request, 'shop.html', {'data': data, 'category': 'Women', 'product_count': women_count})

def collect(request):
    productss = Productz.objects.all()  # Fetch all products (you may want to filter based on category)
    context = {
        'products': productss
    }
    return render(request, 'collections.html', context)

def bag(request):
    return render(request, 'dress.html')

def check(request):
    return render(request, 'check.html')

def cart(request):
    return render(request, 'cart.html')

def ship(request):
    return render(request,'ship.html')
def top(request):
    return render(request,'top.html')

def coat(request):
    return render(request,'coat.html')

def tshirts(request):
    return render(request,'t-shirt.html')

def skirt(request):
    return render(request,'skirt.html')

def bottom(request):
    return render(request,'bottom.html')


#def shop_list(request):
 #   shops = Shops.objects.all()
  #  return render(request, 'shop_list.html', {'shops': shops})
#
#def shop_detail(request, shop_id):
 #   shop = get_object_or_404(Shops, id=shop_id)
  #  categories = Category.objects.filter(shop=shop)
   # products = Productz.objects.filter(shop=shop)
    #return render(request, 'shop_detail.html', {'shop': shop, 'categories': categories, 'products': products})

#def category_detail(request, category_id):
 #   category = get_object_or_404(Category, id=category_id)
  #  products = Productz.objects.filter(category=category)
   # return render(request, 'category_detail.html', {'category': category, 'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Productz, id=product_id)
    return render(request, 'detailproduct.html', {'product': product})

def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, product_id):
    productz = Productz.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(productz=productz,user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('view_cart')

def remove_from_cart(request, product_id):
    cart_item = CartItem.objects.get(id=product_id)
    cart_item.delete()
    return redirect('view_cart')