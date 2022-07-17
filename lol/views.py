from django.shortcuts import render, HttpResponse
from .tasks import add
# Create your views here.
def create_celerytask(request):
    print('开始执行')
    add.delay(2,3)
    print('执行结束')
    return HttpResponse('OK')