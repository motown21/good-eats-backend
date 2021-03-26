from django.urls import path
from .views.dish_views import Dishes, DishDetail
from .views.mango_views import Mangos, MangoDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
  	# Restful routing
    path('dishes/', Dishes.as_view(), name='dishes'),
    path('dishes/<int:pk>/', DishDetail.as_view(), name='dish_detail'),
    path('mangos/', Mangos.as_view(), name='mangos'),
    path('mangos/<int:pk>/', MangoDetail.as_view(), name='mango_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
