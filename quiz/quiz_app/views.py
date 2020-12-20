from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Topic, Question, Choice

# Create your views here.
def index(request):
    return render(request, 'index.html')

class TopicListView(LoginRequiredMixin, ListView):
    context_object_name = "topics"
    model = Topic
    

class TopicDetailView(LoginRequiredMixin, DetailView):
    context_object_name = "topic"
    model = Topic

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
