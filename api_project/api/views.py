from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User

# Create your views here.
class BookList(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class BookAPIView(APIView):
    """
    Example protected view that requires token authentication
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        return Response({
            'message': 'Hello, authenticated user!',
            'user': request.user.username,
            'user_id': request.user.id
        })