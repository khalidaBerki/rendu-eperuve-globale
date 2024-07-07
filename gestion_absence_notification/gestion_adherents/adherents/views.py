from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import Adherent, Presence, Intervenant  # Import du modèle Intervenant
from .serializers import IntervenantSerializer

# Vues pour les adhérents

def index(request):
    return render(request, 'index.html')

@api_view(['GET'])
def list_adherents(request):
    adherents = Adherent.objects.all()
    data = [{'id': adherent.id, 'nom': adherent.nom, 'age': adherent.age, 'adresse': adherent.adresse, 'telephone': adherent.telephone} for adherent in adherents]
    return JsonResponse(data, safe=False)

@api_view(['POST'])
def send_notification_email(request, adherent_id):
    adherent = get_object_or_404(Adherent, pk=adherent_id)

    if adherent.age < 18 and adherent.responsable_legal:
        subject = f'Notification: Absence non justifiée de {adherent.nom}'
        message = f'Bonjour {adherent.responsable_legal.nom},\n\nNous vous informons que {adherent.nom} a une absence non justifiée à un cours. Veuillez contacter l\'association pour plus de détails.\n\nCordialement,\nL\'équipe de gestion des adhérents'
        from_email = settings.EMAIL_HOST_USER
        to_email = [adherent.responsable_legal.email]

        try:
            send_mail(subject, message, from_email, to_email)
            return Response({'message': 'Notification envoyée avec succès'})
        except Exception as e:
            return Response({'message': f'Erreur lors de l\'envoi de la notification : {str(e)}'}, status=500)

    return Response({'message': 'Aucune notification envoyée'})

@api_view(['POST'])
def enregistrer_presences(request):
    data = request.data
    date_today = timezone.now().date()

    try:
        for adherent_id, present in data.items():
            adherent = get_object_or_404(Adherent, id=adherent_id)
            presence, created = Presence.objects.get_or_create(adherent=adherent, date=date_today)
            presence.present = present
            presence.save()

        return Response({"message": "Présences enregistrées avec succès"}, status=201)
    except Exception as e:
        return Response({"error": str(e)}, status=500)

@api_view(['GET'])
def list_presences(request):
    date_today = timezone.now().date()
    presences = Presence.objects.filter(date=date_today)
    data = [{'adherent': presence.adherent.nom, 'present': presence.present} for presence in presences]
    return Response(data)

# Vues pour les intervenants
# adherents/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import Intervenant
from .serializers import IntervenantSerializer

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and isinstance(user, Intervenant):
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

class IntervenantListCreateView(generics.ListCreateAPIView):
    queryset = Intervenant.objects.all()
    serializer_class = IntervenantSerializer
    permission_classes = [IsAuthenticated]

class IntervenantRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Intervenant.objects.all()
    serializer_class = IntervenantSerializer
    permission_classes = [IsAuthenticated]


from django.shortcuts import render
from django.http import HttpResponse
from .utils import set_intervenant_password

def update_password_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        new_password = request.POST.get('new_password')

        if set_intervenant_password(username, new_password):
            return HttpResponse('Mot de passe mis à jour avec succès !')
        else:
            return HttpResponse('Erreur : intervenant non trouvé.')

    return render(request, 'update_password.html')

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response

class MyTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def save_selected_adherents(request):
    if request.method == 'POST':
        data = request.POST
        adherents_present = data.getlist('adherentsPresent[]', [])
        adherents_absent = data.getlist('adherentsAbsent[]', [])

        # Traitez les adhérents présents et absents ici (enregistrement en base de données, traitement, etc.)

        return JsonResponse({'message': 'Adhérents sélectionnés enregistrés avec succès!'})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Adherent

@csrf_exempt
def update_presence(request, adherent_id):
    adherent = get_object_or_404(Adherent, pk=adherent_id)

    if request.method == 'PUT':
        try:
            present = request.data.get('present')
            adherent.present = present
            adherent.save()
            return JsonResponse({'message': f'Présence de {adherent.nom} mise à jour avec succès!'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
