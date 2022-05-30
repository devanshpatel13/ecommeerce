"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from App.views import *
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path("", registrationview, name="regi"),
                  path("login/", loggin, name="login"),
                  path("index/", indexview.as_view(), name="index"),
                  path("home/", home, name="home"),
                  path("list/", indexlistView.as_view(), name="list"),
                  path("update/<int:pk>/", updatepro.as_view(), name="update"),
                  path("delete/<int:id>/", deletepro, name="delete"),
                  path("addtocart/<int:id>/", addtocart, name="addtocart"),
                  path("cart/", cartitemviews, name="cart"),
                  path("minus/<int:id>/", minuscart, name="minus"),
                  path("plus/<int:id>/", pluscart, name="plus"),
                  path("delcart/<int:id>/", deletecart, name="delcart"),
                  path("checkout/", checkout, name="checkout"),
                  path("address/", address, name="address"),
                  path("myorders/", myorder, name="myorders"),
                  # path("placeorder/",placeorder,name = "placeorder"),
                  path("cancel/", cancelview, name="cancel"),
                  path("landing/", landingniew, name="landing"),
                  path('createcheckout/', create_checkout_sessionView.as_view(), name="createcheckout"),
                  path("webhook/",stripe_webhook,name = "webhook")

                  # path("Authc/",Authc,name ="Authc")

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
