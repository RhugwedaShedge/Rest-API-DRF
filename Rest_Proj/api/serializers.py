from rest_framework import serializers
from .models import Task # This is the model that we want to serialize

# Similar to forms
class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__' # Double underscore

