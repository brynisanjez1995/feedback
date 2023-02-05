from .models import Feedback
from rest_framework import generics
from .serializers import FeedbackSerializer



class FeedbackListCreate(generics.ListCreateAPIView):
    serializer_class = FeedbackSerializer
    
    def get_queryset(self):
        qs = Feedback.objects.all()
        if not qs:
            return None
        return qs

class FeedbackRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
