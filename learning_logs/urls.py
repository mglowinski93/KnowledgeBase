from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),#wyszukiwanie pustego wyrazenia regularnego.Znak ^ to poczatek stringu, a $ koniec
    url(r'^topics/', views.topics, name='topics'),
    url(r'^topic/(?P<topic_id>\d)', views.topic, name='topic'),
    url(r'^content/(?P<entry_id>\d)', views.entry_content, name='entry_content'),
    url(r'^new_topic/', views.new_topic, name='new_topic'),
    url(r'^new_entry/(?P<topic_id>\d+)', views.new_entry, name='new_entry'),
    url(r'^edit_entry/(?P<entry_id>\d+)', views.edit_entry, name='edit_entry'),
]