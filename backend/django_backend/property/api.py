from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Property, Reservation
from .serializers import PropertiesListSerializer, PropertiesDetailSerializer, ReservationsSerializer
from .forms import PropertyForm

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def properties_list(request):
    properties = Property.objects.all()
    landlord = request.GET.get('landlord_id', '')
    if landlord:
        properties.filter(landlord_id=landlord)
    serializer = PropertiesListSerializer(properties, many=True)
    return JsonResponse({
        'data': serializer.data
    })

@api_view(['POST'])
def create_property(request):
    form = PropertyForm(request.POST, request.FILES)
    print('Entered the backend function ====')
    if form.is_valid():
        property = form.save(commit=False)
        property.landlord = request.user
        property.save()

        return JsonResponse({'success': True})
    else:
        print('error', form.errors, form.non_field_errors)
        return JsonResponse({'errors': form.errors.as_json()}, status=400)
    
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def properties_detail(request, pk):
    property = Property.objects.get(pk=pk)
    serializer = PropertiesDetailSerializer(property, many=False)
    return JsonResponse(serializer.data)
    
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def reservation_list(request, pk):
    property = Property.objects.get(pk=pk)
    reservations = property.reservations.all()
    serializer = ReservationsSerializer(reservations, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def book_property(request, pk):
    try:
        start_date = request.POST.get('start_date', '')
        end_date = request.POST.get('end_date', '')
        price = request.POST.get('total_price', '')
        number_of_nights = request.POST.get('number_of_nights', '')
        guests = request.POST.get('guests')
        property = Property.objects.get(pk=pk)

        Reservation.objects.create(
            property= property,
            start_date = start_date,
            end_date = end_date,
            total_price = price,
            number_of_nights = number_of_nights,
            guests = guests,
            created_by = request.user
        )
        return JsonResponse({'success': True})
    except Exception as e:
        print('Error')
        return JsonResponse({'success': False})
    
@api_view(['POST'])
def toggle_favorited(request, pk):
    property = Property.objects.get(pk=pk)
    if request.user in property.favorited.all():
        property.favorited.remove(request.user)
        return JsonResponse({"Favorite": False})
    else:
        property.favorited.add(request.user)
        return JsonResponse({'favorited': True})