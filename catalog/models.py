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

    # Product specifications
    movement = models.CharField(
        max_length=100,
        blank=True
    )

    dial = models.CharField(
        max_length=100,
        blank=True
    )

    strap = models.CharField(
        max_length=100,
        blank=True
    )

    case = models.CharField(
        max_length=100,
        blank=True
    )

    water_resistance = models.CharField(
        max_length=100,
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


class Review(models.Model):

    RATING_CHOICES = [
        (1, "1 Star"),
        (2, "2 Stars"),
        (3, "3 Stars"),
        (4, "4 Stars"),
        (5, "5 Stars"),
    ]

    watch = models.ForeignKey(
        Watch,
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    customer_name = models.CharField(max_length=100)

    rating = models.PositiveSmallIntegerField(
        choices=RATING_CHOICES
    )

    review_text = models.TextField()

    customer_photo = models.ImageField(
        upload_to="reviews/",
        blank=True,
        null=True
    )

    is_approved = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.watch.name}"