from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Message
from .serializers import MessageSerializer
from rest_framework import status
from rest_framework.response import Response

@api_view(['GET','POST'])
def send_message(request):

    if request.method == 'GET':
        message = Message.objects.all()
        serializers = MessageSerializer(message,many=True)
        return JsonResponse({'Message': serializers.data})

    elif request.method == 'POST':
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

