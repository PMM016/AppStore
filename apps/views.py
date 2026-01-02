from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse

from .models import App, Category
from .forms import AppForm


def index(request):
    app_list = (
        App.objects
        .prefetch_related("categories")
        .order_by("name")
    )

    paginator = Paginator(app_list, 8)
    page_number = request.GET.get("page")
    apps = paginator.get_page(page_number)

    return render(request, "apps/index.html", {
        "apps": apps
    })


def app_list(request):
    apps = App.objects.prefetch_related("categories").all()
    count = apps.count()

    return render(request, "apps/app_list.html", {
        "apps": apps,
        "count": count,
    })


def category_list(request):
    categories = Category.objects.all()
    apps = App.objects.prefetch_related("categories")
    count = categories.count()

    return render(request, "apps/category_list.html", {
        "apps": apps,
        "categories": categories,
        "count": count,
    })


def app_detail(request, id):
    app = get_object_or_404(
        App.objects.prefetch_related("categories"),
        id=id
    )
    return render(request, "apps/app_detail.html", {
        "app": app
    })


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    app_list = category.apps.all()

    paginator = Paginator(app_list, 8)
    page_number = request.GET.get("page")
    apps = paginator.get_page(page_number)

    return render(request, "apps/category.html", {
        "category": category,
        "apps": apps
    })


def app_create(request):
    form = AppForm(
        request.POST or None,
        request.FILES or None
    )

    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse('<script>location.reload()</script>')

    return render(request, "apps/partials/app_form_modal.html", {
        "form": form,
        "title": "Create App"
    })


def app_edit(request, id):
    app = get_object_or_404(App, id=id)

    form = AppForm(
        request.POST or None,
        request.FILES or None,
        instance=app
    )

    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse('<script>location.reload()</script>')

    return render(request, "apps/partials/app_form_modal.html", {
        "form": form,
        "title": "Edit App"
    })


def app_delete(request, id):
    app = get_object_or_404(App, id=id)

    if request.method == "POST":
        app.delete()
        return redirect("apps:index")

    return render(request, "apps/app_confirm_delete.html", {
        "app": app
    })


def price_list(request):
    apps = App.objects.all()
    count = apps.count()

    return render(request, "apps/app_list.html", {
        "apps": apps,
        "count": count,
    })