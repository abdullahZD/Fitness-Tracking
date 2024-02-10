from django.urls import path
from rest_framework_simplejwt.views import   TokenObtainPairView,  TokenRefreshView , TokenVerifyView
from .views import register_user, user_login, user_logout
from .views import WorkoutListView, WorkoutDetailView, FitnessGoalListView, FitnessGoalDetailView, \
    NotificationListView, NotificationDetailView, ProfileDetailView, ProfileUpdateView

   
  

urlpatterns = [
    #jwt Token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    #Authenticaton
    path('api/register/', register_user, name='register'),
    path('api/login/', user_login, name='login'),
    path('api/logout/', user_logout, name='logout'),

    #EndPoints
    # Workout Endpoints
    path('api/workouts/', WorkoutListView.as_view(), name='workout-list'),
    path('api/workouts/<int:pk>/', WorkoutDetailView.as_view(), name='workout-detail'),

    # Fitness Goal Endpoints
    path('api/fitness-goals/', FitnessGoalListView.as_view(), name='fitness-goal-list'),
    path('api/fitness-goals/<int:pk>/', FitnessGoalDetailView.as_view(), name='fitness-goal-detail'),

    # Notification Endpoints
    path('api/notifications/', NotificationListView.as_view(), name='notification-list'),
    path('api/notifications/<int:pk>/', NotificationDetailView.as_view(), name='notification-detail'),

    # Profile Endpoints
    path('api/profile/', ProfileDetailView.as_view(), name='profile-detail'),
    path('api/profile/update/', ProfileUpdateView.as_view(), name='profile-update'),
]

    
    
