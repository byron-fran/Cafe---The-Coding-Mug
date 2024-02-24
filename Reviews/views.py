from django.views.generic import ListView, FormView
from  .models import Review
from .forms import ReviewForm
from django.shortcuts import redirect
from Auth.models import User
from .mixins import HasReviewMixin

# Create your views here.
class ListComments(ListView):
    template_name = 'reviews.html',
    context_object_name = 'reviews'
    model = Review
    queryset = Review.objects.all()

    
class FormReview(HasReviewMixin, FormView):
    form_class = ReviewForm
    template_name = 'form_review.html'
    login_url = '/accounts/login/'
    success_url = '/'
        
    def form_valid(self, form):
        title = form.cleaned_data['title']
        comment = form.cleaned_data['comment']
        user = self.request.user
  
        existing_review = Review.objects.filter(title=title, user=user).first()

        if existing_review:
           
            existing_review.comment = comment
            existing_review.save()
        else:
           
            new_review = Review(title=title, comment=comment, user=user)
            new_review.save()

        return redirect(self.success_url)
