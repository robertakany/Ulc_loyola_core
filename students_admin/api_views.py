
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from urllib.parse import urlencode
import hashlib
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Souscription


class CallbackAPIView(APIView):
    def post(self, request, souscrip_id):
        data = request.data
        # Vérifier si le statut envoyé est "ok"
        if data.get('status') != "COMPLETED" or not data.get('amount'):
            return Response(
                {"message": "Invalid status. Expected 'ok'."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        # Récupérer le booking
        souscrip = get_object_or_404(Souscription, id=souscrip_id)

        # Vérifier si la réservation n'est pas déjà validée
        if not souscrip.is_paid:
            # Mettre à jour la réservation
            souscrip.is_paid = True
            souscrip.save()


            # Retourner une réponse de succès
            return Response(
                {"message": "Souscription validated and stock updated successfully."},
                status=status.HTTP_200_OK,
            )
        else:
            # Retourner une réponse si la réservation est déjà validée
            return Response(
                {"message": "Booking is already validated."},
                status=status.HTTP_400_BAD_REQUEST,
            )
