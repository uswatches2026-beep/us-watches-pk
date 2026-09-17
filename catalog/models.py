from django.db import models


class Watch(models.Model):

    COLLECTION_CHOICES = [
        ("Classic", "Classic"),
        ("Premium", "Premium"),
        ("Everyday", "Everyday"),
        ("Minimal", "Minimal"),
        ("New Arrivals", "New Arrivals"),
    ]

    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(
        upload_to="watches/",
        blank=True,
        null=True
    )

    collection = models.CharField(
        max_length=100,
        choices=COLLECTION_CHOICES,
        blank=True
    )

    stock = models.PositiveIntegerField(default=0)

    is_featured = models.BooleanField(default=False)
    is_new_arrival = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name