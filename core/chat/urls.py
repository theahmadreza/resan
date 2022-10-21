# for import media as statics
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

from . import views
# create chat urls here.

urlpatterns = [
    path('', views.index, name="home"),

    # for a users chat page.
    path('chat/<str:pk>/', views.chat_page, name="chat-page"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
