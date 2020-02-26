from django.shortcuts import render
from items.models import Item
from .serializers import (
    RegisterSerializer,
    ItemListSerializer,
    ItemDetailSerializer,
)
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
)
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny
from .permissions import IsOwnerOrStaff

class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    permission_classes = [AllowAny]

class ItemDetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'
    permission_classes = [IsOwnerOrStaff]
