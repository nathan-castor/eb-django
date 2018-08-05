"""ebdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from accounts import views as accounts_views
from boards import views


urlpatterns = [
    # portfolio urls
    url(r'^$', views.index, name='index'),
    url(r'^serverless$', views.serverless, name='serverless'),
    url(r'^metabase$', views.metabase, name='metabase'),
    url(r'^boards$', views.home, name='home'),
    # accounts urls
    url(r'^signup/$', accounts_views.signup, name='signup'),
    # url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    # url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # boards urls
    url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    url(r'^admin/', admin.site.urls),
]
#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)