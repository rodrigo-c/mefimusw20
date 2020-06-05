from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from core.models import Submission


class SubmissionCreateView(CreateView):
    model = Submission
    fields = ('title', 'text', 'link','cover_image', 'back_image')
