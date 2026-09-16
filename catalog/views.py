from django.shortcuts import render, get_object_or_404
from .models import Watch


def home(request):
    watches = Watch.objects.all()

    return render(
        request,
        "catalog/home.html",
        {"watches": watches}
    )


def watch_detail(request, watch_id):
    watch = get_object_or_404(Watch, id=watch_id)

    return render(
        request,
        "catalog/watch_detail.html",
        {"watch": watch}
    )