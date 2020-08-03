
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


class TodoList(generics.ListCreateAPIView):
    """
    List of all todo entries, or creating a new todo
    """
    queryset = TodoEntry.objects.all()
    serializer_class = TodoSerializer


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a todo entry
    """
    queryset = TodoEntry.objects.all()
    serializer_class = TodoSerializer


'''
class TodoHighlights(generics.GenericAPIView):
    queryset = TodoEntry.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        todo = self.get_object()
        return Response(todo.highlighted)
        '''


class CategoryList(generics.ListCreateAPIView):
    """
    List of all Categories, or creating a new Categories
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveDestroyAPIView):
    """
    Show or delete a specific Category
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


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
