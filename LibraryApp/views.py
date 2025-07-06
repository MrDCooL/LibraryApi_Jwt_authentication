from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .serializers import AppUserSerializer,BookSerializer,BorrowSerializer
from .models import AppUser,Book,Borrow
from rest_framework.permissions import IsAuthenticated
from .permissions import IsLibrarianOrReadOnly,IsMember
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.


class RegisterView(CreateAPIView):
    querySet = AppUser.objects.all()
    serializer_class = AppUserSerializer



class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def perform_create(self, serializer):
        serializer.save(added_by = self.request.user)

    permission_classes = [IsAuthenticated,IsLibrarianOrReadOnly]



class BorrowViewSet(ModelViewSet):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer
    def perform_create(self, serializer):
        serializer.save(borrower = self.request.user)

    permission_classes = [IsAuthenticated,IsMember]


class logoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        refresh_token = request.data.get('refresh')
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({"detail":"loged out sucessfully"})
        
