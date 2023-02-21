from django.shortcuts import render
from rest_framework.viewsets import ViewSet,ModelViewSet
from . import models,serializers
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView
from blogs import services,models,serializers,repositories

class BlogViewSet(ModelViewSet):
    services=services.BlogServicesV1()
    queryset=models.Blog.objects.all()
    serializer_class=serializers.BlogSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.services.create_blog(data=serializer.validated_data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers)

    def list(self, request, *args, **kwargs):
        queryset = self.services.get_blogs()

        serializer = self.get_serializer(queryset,many=True)
        return Response(serializer.data)








# @api_view(['POST'])
# def create_blog(request):
#     serializer=serializers.BlogSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     blog=models.Blog.objects.create(**serializer.validated_data)
#     # blog_data=request.data
#     # blog=models.Blog.objects.create(title=blog_data['title'],body=blog_data['body']) 
#     #print(blog['title'])
#     return Response(serializer.data)



# @api_view(['GET'])
# def get_blog(request,*args,**kwags):
#     blog=get_object_or_404(models.Blog.objects.all(),**kwags)
#     print(kwags)
#     data=serializers.BlogSerializer(blog).data
#     return Response(data)


# class BlockView(ViewSet):
#     def list(self,request,*args,**kwargs):
#         blog=models.Blog.objects.all()
#         serializer=serializers.BlogSerializer(blog,many=True)
#         return Response(serializer.data)

#     def retrieve(self,request,pk):
#         blogs=models.Blog.objects.all()
#         blog = get_object_or_404(blogs, pk=pk)
#         serializer=serializers.BlogSerializer(blog)
#         return Response(serializer.data)

# class BlockViewSet(ModelViewSet):
#     queryset=models.Blog.objects.all()
#     serializer_class=serializers.BlogSerializer






# def index(request,*args, **kwargs):
#     title=request.GET.get('title')
#     body=request.GET.get('body')

#     # blog=models.Blog.objects.get(id=int(kwargs['id']))
#     # blog_info={
#     #     "blog_id":blog.id,
#     #     "title":blog.title,   
#     # }

#     blog=models.Blog.objects.create(
#         body=body,
#         title=title,
#     )
#     return JsonResponse({
#         'id':blog.id,
#         'title':blog.title,
#         'body':blog.body
#     },safe=False)
