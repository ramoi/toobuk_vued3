"""statist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.conf.urls import url
from django.views.generic import TemplateView
import statist.views as action 
#from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    # path("",
    #     TemplateView.as_view(template_name="application.html"),
    #     name="app",
    # ),
    url(r'^sample$', TemplateView.as_view(template_name='sample.html'), name='sample'),
    url(r'^stock/getStock$', action.getStock),
    url(r'^currency/m2$', action.m2),
    url(r'^debt/gDebt$', action.governmentDebtRatioByGdp),
    url(r'^debt/deptCp$', action.deptCp),
    url(r'^house/getLoc$', action.getLoc),
    url(r'^house/getDate$', action.getDate),
    url(r'^house/getTradeIDRatio$', action.getTradeIDRatio),

    #url(r'^statist$', views.render_statist, name='render_statist'),
]