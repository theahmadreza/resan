from django.urls import path

from . import views
# create chat urls here.

urlpatterns = [
    path('', views.index, name="home"),

    # for a users chat page.
    path('chat/<str:pk>/', views.chat_page, name="chat_page"),
]
