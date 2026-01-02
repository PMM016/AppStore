from django.urls import path
from . import views

app_name = "apps"

urlpatterns = [
    path("", views.index, name="index"),

    # App views
    path("view/<int:id>/", views.app_detail, name="view"),
    path("view/", views.app_list, name="app_list"),

    # Categories
    path("category/", views.category_list, name="category_list"),
    path("category/<slug:slug>/", views.category_detail, name="category_detail"),

    # CRUD
    path("create/", views.app_create, name="create"),
    path("edit/<int:id>/", views.app_edit, name="edit"),
    path("delete/<int:id>/", views.app_delete, name="delete"),

    # Price
    path("price/", views.category_list, name="price_list"),

]
