# Create your views here.
from django.http import HttpResponse
from socialc.helloworld.models import Greetings

def index(request):
    g = Greetings.objects.order_by('?')[0]
    return HttpResponse(g)

