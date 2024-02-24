from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect

class HasReviewMixin(LoginRequiredMixin):
    
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            if request.user.review_set.exists():
                return redirect('/')
        return super().dispatch(request, *args, **kwargs)
