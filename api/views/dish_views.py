from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.dish import Dish
from ..serializers import DishSerializer, UserSerializer

# Create your views here.
class Dishes(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = DishSerializer
    def get(self, request):
        """Index request"""
        # Get all the dishs:
        # dishs = dish.objects.all()
        # Filter the dishs by owner, so you can only see your owned dishs
        dishes = Dish.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = dishSerializer(dishes, many=True).data
        return Response({ 'dishes': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['dish']['owner'] = request.user.id
        # Serialize/create dish
        dish = dishSerializer(data=request.data['dish'])
        # If the dish data is valid according to our serializer...
        if dish.is_valid():
            # Save the created dish & send a response
            dish.save()
            return Response({ 'dish': dish.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(dish.errors, status=status.HTTP_400_BAD_REQUEST)

class DishDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the dish to show
        dish = get_object_or_404(dish, pk=pk)
        # Only want to show owned dishs?
        if not request.user.id == dish.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this dish')

        # Run the data through the serializer so it's formatted
        data = dishSerializer(dish).data
        return Response({ 'dish': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate dish to delete
        dish = get_object_or_404(dish, pk=pk)
        # Check the dish's owner agains the user making this request
        if not request.user.id == dish.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this dish')
        # Only delete if the user owns the  dish
        dish.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Remove owner from request object
        # This "gets" the owner key on the data['dish'] dictionary
        # and returns False if it doesn't find it. So, if it's found we
        # remove it.
        if request.data['dish'].get('owner', False):
            del request.data['dish']['owner']

        # Locate dish
        # get_object_or_404 returns a object representation of our dish
        dish = get_object_or_404(dish, pk=pk)
        # Check if user is the same as the request.user.id
        if not request.user.id == dish.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this dish')

        # Add owner to data object now that we know this user owns the resource
        request.data['dish']['owner'] = request.user.id
        # Validate updates with serializer
        data = DishSerializer(dish, data=request.data['dish'])
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
