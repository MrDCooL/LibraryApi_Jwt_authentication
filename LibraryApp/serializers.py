from .models import AppUser,Book,Borrow
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ValidationError

class AppUserSerializer(ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['username','password','role']

    def create(self,validated_data):
        return AppUser.objects.create_user(**validated_data)

class BookSerializer(ModelSerializer):
    class Meta:
        models = Book
        fields = "__all__"
        read_only_fields = ["added_by"]

    def validate_title(self,value):
        if len(value)<=3:
            raise ValidationError("title cant be less than 3 letters")
        return value

class BorrowSerializer(ModelSerializer):
    class Meta:
        models = Borrow
        fields = "__all__"
        read_only_fields = ['borrower']

    def validate(self, data):
        user = self.context['request'].user
        book = data['book']
        if Borrow.objects.filter(borrower = user,book = book).exists() :
            raise ValidationError('user has already has the book')
        return data

        
        