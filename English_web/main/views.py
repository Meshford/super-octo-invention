from django.shortcuts import render

#те методы которые будут вызвваны при переходе пользователем на разные страницы
# Create your views here.
def index(request): #в любом методе необходим один обязательный параметр это параметр request
    data={
        'title': 'Главная страница',
        'values': ['Some','Hello','123']

    }
    return render(request,'main/index.html',data)


