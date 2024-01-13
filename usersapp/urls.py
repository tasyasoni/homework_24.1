from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from usersapp.apps import UsersappConfig
from usersapp.views import UserCreateAPIView, UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView, \
    UserDestroyAPIView


app_name = UsersappConfig.name


urlpatterns = [
    path('user/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/create/', UserCreateAPIView.as_view(), name='user_create'),
    path('user/list/', UserListAPIView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserRetrieveAPIView.as_view(), name='user_one'),
    path('user/update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('user/delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user_delete'),
]