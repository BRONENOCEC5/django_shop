from rest_framework.generics import (ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, 
                                     DestroyAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.filters import SearchFilter

from products.filters import ProductPriceFilter

from .models import Product, Comment
from .serializers import ProductSerializer, ProductListSerializer, CommentSerializer
from .permissions import IsAuthor

# @api_view(['GET'])
# def products_list(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)

# class ProductsListView(APIView):
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)

# class ProductsListView(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductListSerializer

# class CreateProductView(CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class ProductListCreateView(ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class ProductDetailsView(RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class ProductUpdateView(UpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class ProductDeleteView(DestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class ProductRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description']
    filterset_class = ProductPriceFilter
    permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [permissions]

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return super().get_serializer_class()

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ['destroy', 'update']:
            self.permission_classes = [IsAuthor]
        return super().get_permissions()


#post -> 'create'
#get -> 'list', 'retrieve'
#put -> 'update'
#patch -> 'partial_update'
#delete -> 'destroy'