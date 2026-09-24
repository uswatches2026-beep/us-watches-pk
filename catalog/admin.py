from django.contrib import admin

from .models import Watch, WatchImage, Review


class WatchImageInline(admin.TabularInline):
    model = WatchImage
    extra = 3


@admin.register(Watch)
class WatchAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "collection",
        "price",
        "stock",
        "is_active",
    )

    fieldsets = (
        (
            "Basic Information",
            {
                "fields": (
                    "name",
                    "slug",
                    "description",
                    "image",
                    "collection",
                )
            },
        ),
        (
            "Product Specifications",
            {
                "fields": (
                    "movement",
                    "dial",
                    "strap",
                    "case",
                    "water_resistance",
                )
            },
        ),
        (
            "Inventory",
            {
                "fields": (
                    "price",
                    "stock",
                )
            },
        ),
        (
            "Website Settings",
            {
                "fields": (
                    "is_featured",
                    "is_new_arrival",
                    "is_active",
                )
            },
        ),
        (
            "Dates",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    inlines = [WatchImageInline]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "customer_name",
        "watch",
        "rating",
        "is_approved",
        "created_at",
    )

    list_filter = (
        "is_approved",
        "rating",
        "created_at",
    )

    search_fields = (
        "customer_name",
        "review_text",
        "watch__name",
    )

    list_editable = (
        "is_approved",
    )