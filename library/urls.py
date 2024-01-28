from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('author/', views.author),
    path('books/', views.books),
    path('saveauthor/', views.saveauthor),
    path('authorview/', views.viewauthorfull),
    path('savebook/', views.savebook),
    path('deletebook/<id>', views.deletebook),
    path('author_count/', views.author_count),
    path('book_count/', views.book_count),
    path('suggestionapi/', views.suggestionApi,name="suggestionapi"),
    path('listproductsapi/', views.listProductsApi,name="listproductsapi"),
    #path('paginationApi/',views.paginationApi.as_view(),name="paginationApi")




]
