from django.conf.urls import url
from quiz_app import views

app_name = "quiz_app"

urlpatterns = [    
    url(r'^$', views.TopicListView.as_view(), name="quiz_list"),
    url(r'^(?P<pk>\d+)/$', views.TopicDetailView.as_view(), name="quiz_detail"),
]