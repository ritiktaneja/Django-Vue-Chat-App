from django.conf.urls import include, url
from django.contrib import admin
from chat import views

urlpatterns = [
    url(r'^chat/', include('chat.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^messages/', views.messages, name='messages'),            
    url(r'^message/(?P<selected_user>\w+)/$', views.message, name='messages'),
    url(r'^api/messages/', views.messagesApi, name='messagesApi'),
    url(r'^api/message/(?P<selected_user>\w+)/$', views.messageApi, name='messagesApi'),
]
