from rest_framework import serializers

def validate_non_empty(value):
    """Validator to ensure field is not empty or just whitespace."""
    if not value or not value.strip():
        raise serializers.ValidationError("This field cannot be empty or contain only whitespace.")
    return value.strip()

class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(
        max_length=100,
        min_length=1,
        validators=[validate_non_empty],
        error_messages={
            'max_length': 'Employee name cannot exceed 100 characters.',
            'min_length': 'Employee name must be at least 1 character.',
            'required': 'Employee name is required.',
            'blank': 'Employee name cannot be blank.'
        }
    )
    role = serializers.ChoiceField(
        choices=["admin", "employee"],
        error_messages={
            'required': 'Role is required.',
            'invalid_choice': 'Role must be either "admin" or "employee".'
        }
    )
    room = serializers.CharField(
        max_length=100,
        required=False,
        allow_blank=True,
        error_messages={
            'max_length': 'Room name cannot exceed 100 characters.'
        }
    )

class TaskSerializer(serializers.Serializer):
    title = serializers.CharField(
        max_length=200,
        min_length=1,
        validators=[validate_non_empty],
        error_messages={
            'max_length': 'Task title cannot exceed 200 characters.',
            'min_length': 'Task title must be at least 1 character.',
            'required': 'Task title is required.',
            'blank': 'Task title cannot be blank.'
        }
    )
    assigned_to = serializers.CharField(
        max_length=100,
        min_length=1,
        validators=[validate_non_empty],
        error_messages={
            'max_length': 'Assignee name cannot exceed 100 characters.',
            'min_length': 'Assignee name must be at least 1 character.',
            'required': 'Task must be assigned to someone.',
            'blank': 'Assignee cannot be blank.'
        }
    )
    status = serializers.ChoiceField(
        choices=["working", "paused", "stopped"],
        default="working",
        error_messages={
            'invalid_choice': 'Status must be one of: "working", "paused", or "stopped".'
        }
    )
    room = serializers.CharField(
        max_length=100,
        required=False,
        allow_blank=True,
        error_messages={
            'max_length': 'Room name cannot exceed 100 characters.'
        }
    )

class UpdateSerializer(serializers.Serializer):
    task_id = serializers.CharField(
        max_length=100,
        min_length=1,
        validators=[validate_non_empty],
        error_messages={
            'max_length': 'Task ID cannot exceed 100 characters.',
            'required': 'Task ID is required.',
            'blank': 'Task ID cannot be blank.'
        }
    )
    author = serializers.CharField(
        max_length=100,
        min_length=1,
        validators=[validate_non_empty],
        error_messages={
            'max_length': 'Author name cannot exceed 100 characters.',
            'min_length': 'Author name must be at least 1 character.',
            'required': 'Author name is required.',
            'blank': 'Author name cannot be blank.'
        }
    )
    message = serializers.CharField(
        max_length=500,
        min_length=1,
        validators=[validate_non_empty],
        error_messages={
            'max_length': 'Message cannot exceed 500 characters.',
            'min_length': 'Message must be at least 1 character.',
            'required': 'Message is required.',
            'blank': 'Message cannot be blank.'
        }
    )
