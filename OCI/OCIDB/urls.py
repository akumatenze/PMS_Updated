# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
#from django.contrib import admin
from .views import YourModelViewSet
from rest_framework_simplejwt.views import ( # type: ignore
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'your-models', YourModelViewSet)

#urlpatterns = [
    #path('admin/', include(router.urls)),
#]

from django.urls import path
from .views import UserList, AuthUserLoginView
# from .views import UserCreateAPIView, UserDetailAPIView, ObtainAuthToken

urlpatterns = [
    path("register/", UserList.as_view(), name = "register"),
    path('login/', AuthUserLoginView.as_view(), name = "login"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/users/', UserCreateAPIView.as_view(), name='user-create'),
    # path('api/users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    # path('api/token/', ObtainAuthToken.as_view(), name='obtain-token'),
]


from django.urls import path
from .views import UserCreateAPIView, UserLoginAPIView

urlpatterns = [
    path('users/register/', UserCreateAPIView.as_view(), name='user_register'),
    path('users/login/', UserLoginAPIView.as_view(), name='user_login'),
]
