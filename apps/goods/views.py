from django.http import HttpResponse


a = 111
def test(request):
    return HttpResponse('test',a)
