from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^submit$', views.submit_idea),
    url(r'^vote$', views.vote_idea),
    url(r'^(?P<pk>\w*)$', views.get_ideas),
]
