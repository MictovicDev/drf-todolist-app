
from rest_framework import pagination


class CustomPageNumberPagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param='count'
    next_page_size=5
    page_query_param = 'p'
