from rest_framework import viewsets
from django.shortcuts import render
from .serializers import UoSerializer
from .models import Tblfop, Tbluo
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import pagination
from rest_framework import filters
# Create your views here.

class PageNumberSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
   #  ordering = 'id'

class UoViewSet(viewsets.ModelViewSet):
    search_fields = ['activity_kinds']
    filter_backends = (filters.SearchFilter,)
    serializer_class = UoSerializer
    queryset = Tbluo.objects.all()
    lookup_field = 'id'
    permission_classes = [permissions.AllowAny]
    pagination_class = PageNumberSetPagination
