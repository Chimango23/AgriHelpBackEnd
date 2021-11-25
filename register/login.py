from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Farmer

@api_view(['GET', 'POST'])
def farmers_auth(request):
    print(request.data)
    if request.method == 'POST':
        username = request.data['username']
        passkey = request.data['password']
        user = Farmer.objects.get(username=username)
        if passkey == user.password:
            return Response(True)
        else:
            return Response(False) 
