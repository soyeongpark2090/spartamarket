from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path('', views.products_list, name="products_list"),
    #
    path('<int:pk>/', views.product_detail, name="product_detail"),
    path('create/', views.create, name="create"),
    path('<int:pk>/delete/', views.delete, name="delete"),
    path('<int:pk>/update/', views.update, name="update"),
    path('<int:pk>/like/', views.like, name="like"),
    #
    path('<int:pk>/create_comment/', views.create_comment, name="create_comment"),
    path('<int:pk>/delete/<int:comment_pk>/',
         views.delete_comment, name="delete_comment"),
]
