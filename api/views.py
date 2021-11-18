from rest_framework import viewsets
from django.shortcuts import render
from .serializers import UoSerializer
from .models import Tblfop, Tbluo
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import pagination
from rest_framework import filters
from rest_framework import pagination
from rest_framework.pagination import CursorPagination


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = None
    max_page_size = 100


def paginate_queryset(self, queryset, request, view=None):
    from django.core.cache import cache

    cache_key = request.path
    skipGetKeys = ['offset', 'limit']
    filter_query = [key + value for key, value in request.GET.iteritems() if key not in skipGetKeys]
    cache_key += '_'.join(filter_query)

    self.count = cache.get(cache_key)

    if self.count == None:
        self.count = self.get_count(queryset)
        cache.set(cache_key, self.count, None)


class CursorSetPagination(CursorPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    ordering = 'id'


class CustomLimitPagination(pagination.LimitOffsetPagination):
    default_limit = 10
    limit_query_param = 'l'
    offset_query_param = 'o'
    max_limit = 100

    def get_paginated_response(self, data):
        return Response({
            'results': data
        })


class CustomPagination2(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })


class PageNumberSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    # ordering = 'id'


class UoViewSet(viewsets.ModelViewSet):
    search_fields = ['address', 'activity_kinds', 'name', 'edrpou']
    filter_backends = (filters.SearchFilter,)
    serializer_class = UoSerializer
    queryset = Tbluo.objects.all()
    lookup_field = 'id'
    permission_classes = [permissions.AllowAny]
    pagination_class = StandardResultsSetPagination
