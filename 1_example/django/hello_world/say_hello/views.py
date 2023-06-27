from django.http import HttpResponse
def say_hello(request):
    '''basic response test'''
    print("request:")
    print(request.body)
    return HttpResponse("Hello world ")