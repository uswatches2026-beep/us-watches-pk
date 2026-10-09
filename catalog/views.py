from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, JsonResponse
from django.utils.text import slugify
from .models import Watch


def maintenance(request):
    return render(request, "catalog/maintenance.html")


def home(request):
    collection = request.GET.get("collection")

    watches = Watch.objects.filter(is_active=True)

    if collection:
        watches = watches.filter(collection=collection)

    collections = [
        "Classic",
        "Premium",
        "Everyday",
        "Automatic",
        "Chronograph",
        "Leather Strap",
        "Limited Edition",
    ]

    cart = request.session.get("cart", {})
    cart_count = sum(cart.values())

    return render(
        request,
        "catalog/home.html",
        {
            "watches": watches,
            "collections": collections,
            "selected_collection": collection,
            "cart_count": cart_count,
        }
    )



def collection_detail(request, collection_slug):
    collection_names = {
        slugify(label): label
        for _, label in Watch.COLLECTION_CHOICES
    }

    collection_name = collection_names.get(collection_slug)
    if not collection_name:
        raise Http404("Collection not found")

    watches = Watch.objects.filter(is_active=True)
    if collection_name != "Full Collection":
        watches = watches.filter(collection=collection_name)

    descriptions = {
        "Full Collection": "Explore every available US Watches timepiece.",
        "Classic": "Timeless designs with a refined character.",
        "Premium": "Distinctive pieces with elevated finishes and presence.",
        "Everyday": "Versatile timepieces designed for everyday moments.",
        "Automatic": "Mechanical timepieces with enduring character and movement.",
        "Chronograph": "Detailed timepieces with a distinctive chronograph presence.",
        "Leather Strap": "Refined leather finishes paired with timeless style.",
        "Limited Edition": "Distinctive pieces from our more exclusive collection.",
    }

    cart = request.session.get("cart", {})
    cart_count = sum(cart.values())

    return render(
        request,
        "catalog/collection.html",
        {
            "collection_name": collection_name,
            "collection_description": descriptions.get(collection_name, "Explore this US Watches collection."),
            "watches": watches,
            "cart_count": cart_count,
        },
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


def add_to_cart(request, watch_id):
    watch = get_object_or_404(
        Watch,
        id=watch_id,
        is_active=True
    )

    cart = request.session.get("cart", {})
    watch_id_str = str(watch.id)

    current_quantity = cart.get(watch_id_str, 0)

    if current_quantity < watch.stock:
        cart[watch_id_str] = current_quantity + 1

    request.session["cart"] = cart
    request.session.modified = True

    cart_count = sum(cart.values())

    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return JsonResponse({
            "success": True,
            "cart_count": cart_count,
            "quantity": cart.get(watch_id_str, 0),
            "stock": watch.stock,
        })

    return redirect(request.META.get("HTTP_REFERER", "home"))


def cart(request):
    cart_data = request.session.get("cart", {})

    cart_items = []
    total = 0

    for watch_id, quantity in cart_data.items():
        watch = Watch.objects.filter(
            id=watch_id,
            is_active=True
        ).first()

        if watch and watch.stock > 0:
            quantity = min(quantity, watch.stock)

            subtotal = watch.price * quantity
            total += subtotal

            cart_items.append({
                "watch": watch,
                "quantity": quantity,
                "subtotal": subtotal,
            })

    return render(
        request,
        "catalog/cart.html",
        {
            "cart_items": cart_items,
            "total": total,
        }
    )


def update_cart(request, watch_id):
    if request.method == "POST":
        watch = get_object_or_404(
            Watch,
            id=watch_id,
            is_active=True
        )

        try:
            quantity = int(request.POST.get("quantity", 1))
        except (TypeError, ValueError):
            quantity = 1

        cart = request.session.get("cart", {})
        watch_id_str = str(watch.id)

        if quantity <= 0:
            cart.pop(watch_id_str, None)
        else:
            quantity = min(quantity, watch.stock)

            if quantity > 0:
                cart[watch_id_str] = quantity
            else:
                cart.pop(watch_id_str, None)

        request.session["cart"] = cart
        request.session.modified = True

    return redirect("cart")


def remove_from_cart(request, watch_id):
    cart = request.session.get("cart", {})
    watch_id_str = str(watch_id)

    current_quantity = cart.get(watch_id_str, 0)

    if current_quantity > 1:
        cart[watch_id_str] = current_quantity - 1
    else:
        cart.pop(watch_id_str, None)

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("cart")