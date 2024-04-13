from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import UserSerializer
from .models import User
from property.serializers import ReservationsSerializer

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def user_detail(request, pk):
    user = User.objects.get(pk=pk)
    serializer = UserSerializer(user, many=False)
    return JsonResponse(serializer.data)

@api_view(['GET'])
def reservations_list(request):
    print("Before anything in reservations")
    reservations = request.user.reservations.all()
    print('Reservations == ', reservations)
    serializer = ReservationsSerializer(reservations, many=True)
    return JsonResponse(serializer.data, safe=False)