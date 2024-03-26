from django.db import models

# Create your models here.


class Wish(models.Model):
    author = models.CharField(max_length=255)
    wish = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.wish}-{self.author}"


class RSVP(models.Model):
    ATTENDING_OPTIONS = (
        ("Có", "Có"),
        ("Không", "Không")
    )
    PARTY_OPTIONS = (
        ("Nhà Trai", "Nhà Trai"),
        ("Nhà Gái", "Nhà Gái"),
        ("Cả Hai", "Cả Hai")
    )
    name = models.CharField(max_length=255)
    num_guests = models.IntegerField(default=1)
    attendance = models.CharField(max_length=10, choices=ATTENDING_OPTIONS, default="Có")
    party = models.CharField(max_length=10, choices=PARTY_OPTIONS, default="Cả Hai")
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}-{self.email}"
