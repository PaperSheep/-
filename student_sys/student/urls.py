from django.urls import path
from . import views


urlpatterns = [
    # path('', views.index, name='index'),  # 使用下面用类封装的方法
    path('', views.IndexView.as_view(), name='index'),
]
