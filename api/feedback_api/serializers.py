from rest_framework import serializers
from .models import Feedback

class FeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = ['id', 'comments', 'status', 'assigned_to', 'customer_id', 'service_id']