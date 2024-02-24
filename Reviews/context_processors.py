from .models import Review

def all_reviews(request):
    reviews = Review.objects.all()
    return {
        "reviews" : reviews
    }