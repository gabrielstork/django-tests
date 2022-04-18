from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register('accounts', views.AccountViewSet)
router.register('posts', views.PostViewSet)
router.register('comments', views.CommentViewSet)
