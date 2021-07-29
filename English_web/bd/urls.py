from django.urls import path
from . import views #из той же папки вызываем views
#здесь мы можем прописать отслеживание отдельных url адресов (отслеживаем прееходы по url адресам)
urlpatterns = [
    path('', views.bd_home, name='v')
]