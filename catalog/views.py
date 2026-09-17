from django.shortcuts import render, get_object_or_404
from .models import Watch


def home(request):
    collection = request.GET.get("collection")

    watches = Watch.objects.filter(is_active=True)

    if collection:
        watches = watches.filter(collection=collection)

    collections = [
        "Classic",
        "Premium",
        "Everyday",
        "Minimal",
        "New Arrivals",
    ]

    return render(
        request,
        "catalog/home.html",
        {
            "watches": watches,
            "collections": collections,
            "selected_collection": collection,
        }
    )


def watch_detail(request, watch_id):
    watch = get_object_or_404(
        Watch,
        id=watch_id,
        is_active=True
    )

    return render(
        request,
        "catalog/watch_detail.html",
        {"watch": watch}
    )