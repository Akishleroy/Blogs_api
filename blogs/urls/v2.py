from django.contrib import admin
from django.urls import path,include
from blogs import views
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register(r'blogs',views.BlogViewSet,'blogs')

urlpatterns = [
    # path('<int:id>/',views.get_blog),
    # path('',views.create_blog),
    path('',include(router.urls)),
    # path('v2/',views.BlockView.as_view({'get':'list'})),
    # path('v2/<int:pk>/',views.BlockView.as_view({'get':'retrieve'}))

]
