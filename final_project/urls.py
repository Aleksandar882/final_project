"""final_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from final_app.views import index
from final_app.views import badges
from final_app.views import topic1
from final_app.views import topic2
from final_app.views import loginPage 
from final_app.views import register 
from final_app.views import logoutUser
from final_app.views import topics
from django.conf import settings
from django.conf.urls.static import static
from final_project.settings import MEDIA_ROOT  
urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , index ,name='index' ),
    path('index/' , index ,name='index' ),
    path('login/' , loginPage ,name='login' ),
    path('register/' , register ,name='register' ),
    path('logout/' , logoutUser ,name='logout' ),
    path('topics/' , topics ,name='topics' ),
    path('topic1/' , topic1 ,name='topic1' ),
    path('topic2/' , topic2 ,name='topic2' ),
    path('badges/' , badges ,name='badges' ),
]+static(settings.MEDIA_URL, document_root=MEDIA_ROOT)
