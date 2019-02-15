from django.conf.urls import url
from . import views

app_name = 'stock'

urlpatterns = [
    url(r'^$', views.render_stock, name='render_stock'),
    #url(r'^sample/$', views.render_stock, name='render_stock')
]

