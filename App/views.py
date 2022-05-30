

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import razorpay
import stripe
import slug as slug
from social_core.pipeline import user
from django.conf import settings
from .models import *
from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views import View
from django.http import HttpResponse
User = get_user_model()


stripe.api_key= settings.STRIPE_SECRET_KEY

#
# def index(request):
#     if request.method == "POST":
#         form = Shopownerform(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("index")
#     else:
#         form = Shopownerform()
#     return render(request, "App/index.html", {'form': form})


class indexview(CreateView):
    template_name = 'App/index.html'
    form_class = Shopownerform
    success_url = '/list/'


class indexlistView(ListView):
    model = Shopowner


class updatepro(UpdateView):
    model = Shopowner
    fields = '__all__'
    success_url = "/list/"


def deletepro(request, id):
    data = Shopowner.objects.get(id=id)
    data.delete()
    return redirect("list")


# def updatepro(request,id):
#     getdata = Shopowner.objects.get(id=id)
#     data = Shopowner.objects.all()
#     if request.method=="POST":
#         form = Shopownerform(request.POST,request.FILES , instance=getdata)
#         if form.is_valid():
#             form.save()
#             return redirect("list")
#     else:
#         form = Shopownerform(instance=getdata)
#     con={"form":form,"data":data}
#
#     return render(request,"App/index.html",con)

#
# def update(request, id):
#     data = Shopowner.objects.all()
#     getdata = Shopowner.objects.get(id=id)
#     if request.method == "POST":
#         form = Shopownerform(request.POST,request.FILES, instance=getdata)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "update successfully")
#             return redirect("home")
#         else:
#             form = Shopownerform(instance=getdata,)
#     else:
#         form = Shopownerform(instance=getdata)
#     con = {"data": data, "form": form}
#     return render(request, "App/index.html", con)
#


# def registrationview(request):
#     # form = Customerform()
#     if request.method == "POST":
#         # form = Customerform(request.POST)
#         # if form.is_valid():
#         print(request.POST, 'formmmmmmmmmmm')
#         user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password1'],
#                                         users=request.POST['users'])
#         user.save()
#         return redirect("login")
#     else:
#         form = Customerform()
#     con = {"form": form}
#     return render(request, "App/registration.html", con)


def registrationview(request):
    if request.method=="POST":
        form = Customerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = Customerform()
    con ={"form":form}
    return render(request, "App/registration.html", con)


def loggin(request):
    print(request.user.is_authenticated)
    #
    # if request.method == "POST":
    #     # print(request.method,request.POST,'=================')
    #     uname = request.POST['username']
    #     upass = request.POST['password']
    #     print(uname, upass, 'paassssssss')
    #     user = authenticate(request, username=uname, password=upass)
    #
    #     print(user.users, 'usrerrrrrrrrrrrrrrrrrr')
    #     if user.users == 'customer':
    #         return redirect("/home/")
    #     else:
    #         return redirect("/index/")
    # else:
    #     form = loginform()

        # if request.method == 'POST':

        #     # print(request.user,'===========HHHHHHHHHHHH======')

        # uname = request.POST['username']
        # upass = request.POST['password']
        #     data = request.POST['users']
        #     print(data,"ttttttttttttttttttttttttttttttttttttttttttttttt")
        # user = authenticate(username=uname,password=upass)
        #     print(user,"dddddddddddddddddddddddddddddddddddddddddddddd")
        #     if user is None:
        #         messages.error(request,'Please Enter Correct Credinatial')
        #         return redirect('login')
        #     else:
        #         # print(request.read(),'===========HHHHHHHHHHHH======')

        # login(request,user)
        #     return redirect('index')
        # else:
        #     if request.user.is_authenticated:
        #         return redirect('index')
        #     else:
        #         pass
    # print(request.user.is_authenticated)
    form = loginform(request.POST)

    if request.method =="POST":
        uname = request.POST['username']
        upass = request.POST['password']
        user = authenticate(username = uname ,password = upass)
        if user is None:
            return redirect("login")
        else:
                login(request,user)
                if request.user.is_authenticated and user.users == 'customer':
                  return redirect("home")
                else:
                    return redirect("index")


    con ={"form":form}



    return render(request, "App/login.html",con)


#
# def index(request):
#     # if request.user.is_authenticated:
#         form = Shopownerform()
#         if request.method == "POST":
#             form = Shopownerform(request.POST)
#             if form.is_valid():
#                 print(form,"ddddddddddddddddddddddddddddddddddddddddddddddddd")
#
#                 form.save()
#
#                 return redirect("index")
#             else:
#                 form = Shopownerform()
#                 return redirect("index")
#         con ={"form":form}
#
#         return render(request,"App/index.html",con)
#
#
# def index(request):
#     print(request, "dddddddddddddddddddddddddddddddd")
#
#     # if request.method =="POST":
#
#     # form = Shopownerform()
#     # if form.is_valid():
#     #     form.save()
#     # con = {"form": form}
#     return render(request, "App/index.html")


#
# def Authc(request):
#     if request.method == "POST":
#         # print(request.method,request.POST,'=================')
#         uname = request.POST['username']
#         upass = request.POST['password']
#         print(uname,upass,'paassssssss')
#         user = authenticate(request,username=uname,password=upass)
#         print(user.users,'usrerrrrrrrrrrrrrrrrrr')
#         if user.users=='customer':
#             return redirect("/home/")
#         else:
#             return redirect("/index/")


def home(request):

    print(request.user.is_authenticated)

    data = Shopowner.objects.all()
    con = {"data": data}

    return render(request, "App/home.html", con)


def addtocart(request,id):

    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        quantity = 1
        user = request.user
        print(user,"ttttttttttttttttttttt")
        single_prod = Shopowner.objects.get(id=id)
        print(single_prod,"vvvvvvvvvvvvvvv")
        try:
            cart_id = Cart.objects.get(user=request.user)
        except Exception :
            data = Cart.objects.create(user=request.user)


        cart_exit = cart_item.objects.filter(user=request.user, product__id=id).exists()
        print(cart_exit,"ffffffffffff")
        if cart_exit:
            cart = cart_item.objects.filter(user=request.user, product__id=id)

            for x in cart:
                x.quantity += 1
                x.save()

        else:
            if single_prod:
                print(single_prod, "vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
                cart = cart_item(user=user, product=single_prod,cart_id=cart_id.id, quantity=quantity).save()

            else:
                pass
            print(cart_id.id,"aaaaaaaaaaaaa")

    return redirect("cart")
    # print(id,"dddddddddddddddd")


def cartviews(request):

    return render(request, "App/shopping_cart.html")


def cartitemviews(request,):
    print(id,"fffffffffffffffff")
    print(request.user.is_authenticated)
    # data= Cart.objects.get(id=id)
    cart = cart_item.objects.filter(user=request.user)
    # data = Cart.objects.create(user=request.user)
    # print(cart.id)


    list1 = []
    list2 = []
    list3 = []
    sub_total = 0
    discount_price = 0
    original_price = 0
    total = 0

    for x in cart:
        list3.append(x.Or_price)
        list2.append(x.total_save)
        list1.append(x.product_total)
        sub_total = sum(list1)
        discount_price = sum(list2)
        original_price = sum(list3)
        total = sub_total
        print(total, "dddddddddddddddddddd")

    con = {"cart": cart, 'sub_total': sub_total, 'total': total,
           "original_price": original_price, "discount_price": discount_price}
    return render(request, "App/shopping_cart.html", con)


#
# def placeorder(request):
#     quantity = 1
#     data = Cart.objects.filter(user=request.user)
#     # cart = Shopowner.objects.filter()
#     # if data:
#     #          Myorder(user=request.user,product = ,quantity=quantity).save()
#
#     cart_data = Cart.objects.filter(user=request.user)
#     add_id = request.POST.get('address_id')
#     couponcode = request.GET.get('code')
#     print(couponcode, "ddddddddddddddddddddddddd")
#
#
#     # customer_add = Address.objects.get(id=add_id)
#     list1 = []
#     list2 = []
#     list3 = []
#     sub_total = 0
#     discount_price = 0
#     original_price = 0
#     total = 0
#     for x in data:
#         list3.append(x.Or_price)
#         list2.append(x.total_save)
#         list1.append(x.product_total)
#         sub_total = sum(list1)
#         total = sub_total
#     if couponcode:
#         print(couponcode, "ddddddddddddddddddddddddddddd")
#         coupon = Couponcode.objects.filter(code=couponcode).first()
#         print(coupon, "ffffffffffffffffffffffffffffffffffffffffffffffffffffffff")
#
#         x = (sub_total * coupon.discount / 100)
#         # total = int(total) * 100
#         print(x, "dddddddddddddddddd")
#         total = total - x
#
#
#     # checkout details
#
#     data = Cart.objects.filter(user=request.user)
#     for i in data:
#         order_data = Myorder(
#             user=request.user,
#             product=i.product,
#             quantity=i.quantity,
#
#         )
#         order_data.save()
#         messages.success(request, 'Your Order Successfully Placed Thank you shoping With us')
#     cart_data.delete()
#     # Pament End
#     return redirect('/landing/')

def landingniew(request):
    return render(request,"App/landing_page.html")


class create_checkout_sessionView(View):
    def post(self, request, *args, **kwargs):
        print(request,"sssssssssssssssssss")
        print(request.user,"?????????????????????")

        print(dict(request.POST.items()),"fffffffffffffffff")
        # product_id = self.kwargs['id']
        # print(product_id,"??????????????????????????")
        cart = cart_item.objects.filter(user=request.user)
        print(cart,"ddddddd")

        quantity = 1
        data = cart_item.objects.filter(user=request.user)


        cart_data = Cart.objects.filter(user=request.user)
        add_id = request.POST.get('address_id')
        couponcode = request.GET.get('code')
        print(couponcode, "ddddddddddddddddddddddddd")

        # customer_add = Address.objects.get(id=add_id)
        list1 = []
        list2 = []
        list3 = []
        sub_total = 0
        discount_price = 0
        original_price = 0
        total = 0
        for x in data:
            list3.append(x.Or_price)
            list2.append(x.total_save)
            list1.append(x.product_total)
            sub_total = sum(list1)
            total = sub_total
        if couponcode:
            print(couponcode, "ddddddddddddddddddddddddddddd")
            coupon = Couponcode.objects.filter(code=couponcode).first()
            print(coupon, "ffffffffffffffffffffffffffffffffffffffffffffffffffffffff")

            x = (sub_total * coupon.discount / 100)
            # total = int(total) * 100
            print(x, "dddddddddddddddddd")
            total = total - x

        # checkout details

        data = cart_item.objects.filter(user=request.user)
        for i in data:
            order_data = Myorder(
                user=request.user,
                product=i.product,
                quantity=i.quantity,
            )

            print(order_data,"order dataaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

            order_data.save()
            messages.success(request, 'Your Order Successfully Placed Thank you shoping With us')
        cart_data.delete()
        # Pament End

        YOUR_DOMAIN = "http://localhost:8000"
        user = request.user
        checkout_session = stripe.checkout.Session.create(
            payment_method_types =['card'],
            line_items=[
                {
                    'name': user,
                    'amount': total,
                    'currency': 'INR',
                    'quantity': 1,


                 },
            ],
            mode='payment',
            success_url= "http://localhost:8000/myorders/",

            cancel_url="http://localhost:8000/cancel/",
            )
        print(user,"vvvvvvvvvvvvvvvvvvv")
        return JsonResponse({
            'id':checkout_session.url

        })






def minuscart(request, id):
    cart = cart_item.objects.filter(id=id)
    for x in cart:
        x.quantity -= 1
        x.save()
    if x.quantity == 0:
        x.delete()

    return redirect("/cart/")


def pluscart(request, id):
    cart = cart_item.objects.filter(id=id)
    for x in cart:
        x.quantity += 1
        x.save()

    return redirect("/cart/")


def deletecart(requets, id):
    cart = cart_item.objects.get(id=id)
    cart.delete()
    return redirect("/cart/")


def address(request):
    if request.method == "POST":
        form = addressform(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            # messages.success(request,{fname,"saved successfully"})
            return redirect('/home/')
    else:
        form = addressform()
        con = {'form': form}
    return render(request, "App/address.html", con)


def checkout(request):
    print(request.user.is_authenticated)


    prod = cart_item.objects.filter(user=request.user)
    print(request.user,"bbbbbbbbbbbbbbbbbbbbbbbb")
    add = Address.objects.filter(user=request.user)
    couponcode = request.GET.get('code')
    print(couponcode, "ddddddddddddddddddddddddd")

    coupon_code_error = None
    coupon = None
    list1 = []
    list2 = []
    list3 = []
    sub_total = 0
    discount_price = 0
    original_price = 0
    shipping_charges = 0.00
    total = 0

    for x in prod:
        list3.append(x.Or_price)
        list2.append(x.total_save)
        list1.append(x.product_total)
        sub_total = sum(list1)
        discount_price = sum(list2)
        original_price = sum(list3)
        total = sub_total
        print(total,"sssssssssssssssssssssss")

    if couponcode:
        print(couponcode, "ddddddddddddddddddddddddddddd")
        coupon = Couponcode.objects.filter(code=couponcode).first()
        print(coupon, "ffffffffffffffffffffffffffffffffffffffffffffffffffffffff")

        x=(sub_total * coupon.discount / 100)
        # total = int(total) * 100
        print(x, "dddddddddddddddddd")
        total = total-x
        coupon_code_error = 'Invalid coupon code'
        print("coupon code invild")

    con = {"prod": prod, 'sub_total': sub_total, 'total': total, "shipping_charges": shipping_charges, "coupon": coupon,
           "coupon_code_error": coupon_code_error, "original_price": original_price, "discount_price": discount_price}

    print("=============", con)

    return render(request, "App/checkout.html", con)


def myorder(request):
    print(request,"11111111111111111111")
    print(request.user," my order user")
    order = Myorder.objects.filter(user=request.user)
    con = {"order": order}
    return render(request, "App/myorders.html", con)


def cancelview(request):
    return render(request,"cancel.html")


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    # sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    # event = None


#     try:
#         event= stripe.webhook.construct_event(
#             payload,sig_header,settings.STR
#
# #         )

    print(payload)

    return HttpResponse(status=200)