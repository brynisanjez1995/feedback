from django.urls import include, path
from .views import FeedbackListCreate, FeedbackRetrieveUpdateDelete

urlpatterns = [
    path('', FeedbackListCreate.as_view() ),
    path('<int:pk>', FeedbackRetrieveUpdateDelete.as_view())
]