
from todo.models import TodoEntry, Category
from todo.serializers import TodoSerializer, CategorySerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers, viewsets

# Create your views here.


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'todo_list': reverse('todo_list', request=request, format=format),
        'categories': reverse('category_list', request=request, format=format)
    })


class TodoViewSet(viewsets.ModelViewSet):
    '''
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions
    '''

    queryset = TodoEntry.objects.all()
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        serializer.save()


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save()
