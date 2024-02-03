from django.contrib import admin
from django.urls import path
from cmpress import views

urlpatterns = [
    path('', views.begin, name='begin'),
    path('new/', views.new, name='home'),
    path('login/', views.login_, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout_, name="logout"),
    path('otp1_/', views.otp1_, name="otp1_"),
    path('otp2_/', views.otp2_, name="otp2_"),
    path('loginnext/', views.afterlogin,name="afterlogin"),
    path('forgot/',views.forgot,name='forgot'),
    path('for_to_otp',views.for_to_otp,name='for_to_otp'),
    path('change_pwd/',views.change_pwd,name='change_pwd'),
    path('sports/',views.sports,name='sports'),
    path('itemlist1/',views.itemlist1,name='itemlist1'),
    path('itemlist2/', views.itemlist2, name='itemlist2'),
    path('itemlist3/', views.itemlist3, name='itemlist3'),
    path('itemlist4/', views.itemlist4, name='itemlist4'),
    path('itemlist5/', views.itemlist5, name='itemlist5'),
    path('itemlist6/', views.itemlist6, name='itemlist6'),
    path('button_action',views.button_action,name='button_action'),
    path('borrow', views.borrow, name='borrow'),

]

