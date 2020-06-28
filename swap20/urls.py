"""swap20 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from core.views import GroupView, MixCreateView, MixView, MixEditView, TagAutocomplete, TagView, home, wall, sendcomment

urlpatterns = [
    path('', home, name='home'),
    path('wall', wall, name='wall'),
    path('sendcomment', sendcomment, name='sendcomment'),
    path('mix/create', MixCreateView.as_view(), name='mixcreate'),
    path('mix/edit/<int:pk>/', MixEditView.as_view(), name='mixedit'),
    path('group/<int:pk>/', GroupView.as_view(), name='group'),
    path('tag/<slug:slug>/', TagView.as_view(), name='tag'),
    path('mix/<int:pk>/', MixView.as_view(), name='mix'),
    path('tag-autocomplete/', TagAutocomplete.as_view(create_field='title'), name='tag-autocomplete'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
