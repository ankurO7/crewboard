from rest_framework import serializers

class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    role = serializers.ChoiceField(choices=["admin", "employee"])
    room = serializers.CharField(max_length=100, required=False, allow_blank=True)

class TaskSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    assigned_to = serializers.CharField(max_length=100)  # employee name or id
    status = serializers.ChoiceField(choices=["working", "paused", "stopped"], default="working")
    room = serializers.CharField(max_length=100, required=False, allow_blank=True)

class UpdateSerializer(serializers.Serializer):
    task_id = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    message = serializers.CharField(max_length=500)