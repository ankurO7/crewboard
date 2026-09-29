import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmployeeSerializer, TaskSerializer, UpdateSerializer
from .mongo import db
from .exceptions import InvalidObjectId, ResourceNotFound, DatabaseError
from .utils import validate_object_id, serialize_mongo_doc

logger = logging.getLogger(__name__)

class EmployeeListCreateView(APIView):
    """Handles employee list retrieval and creation."""
    
    def get(self, request):
        """Retrieve all employees."""
        try:
            employees = list(db.employees.find())
            return Response(
                serialize_mongo_doc(employees),
                status=status.HTTP_200_OK
            )
        except Exception as e:
            logger.error(f"Error fetching employees: {str(e)}")
            raise DatabaseError(detail="Failed to retrieve employees. Please try again.")
    
    def post(self, request):
        """Create a new employee."""
        try:
            serializer = EmployeeSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(
                    {
                        "error": "Validation failed",
                        "details": serializer.errors
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            data = dict(serializer.validated_data)
            result = db.employees.insert_one(data)
            data["_id"] = str(result.inserted_id)
            
            return Response(
                {
                    "message": "Employee created successfully",
                    "data": data
                },
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            logger.error(f"Error creating employee: {str(e)}")
            raise DatabaseError(detail="Failed to create employee. Please try again.")

class TaskListCreateView(APIView):
    """Handles task list retrieval and creation."""
    
    def get(self, request):
        """Retrieve all tasks."""
        try:
            tasks = list(db.tasks.find())
            return Response(
                serialize_mongo_doc(tasks),
                status=status.HTTP_200_OK
            )
        except Exception as e:
            logger.error(f"Error fetching tasks: {str(e)}")
            raise DatabaseError(detail="Failed to retrieve tasks. Please try again.")
    
    def post(self, request):
        """Create a new task."""
        try:
            serializer = TaskSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(
                    {
                        "error": "Validation failed",
                        "details": serializer.errors
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            data = dict(serializer.validated_data)
            result = db.tasks.insert_one(data)
            data["_id"] = str(result.inserted_id)
            
            return Response(
                {
                    "message": "Task created successfully",
                    "data": data
                },
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            logger.error(f"Error creating task: {str(e)}")
            raise DatabaseError(detail="Failed to create task. Please try again.")

class TaskStatusUpdateView(APIView):
    """Handles task status updates."""
    
    VALID_STATUSES = ["working", "paused", "stopped"]
    
    def patch(self, request, task_id):
        """Update task status."""
        try:
            # Validate task ID
            valid_id = validate_object_id(task_id, "task_id")
            
            # Validate status
            new_status = request.data.get("status")
            if not new_status:
                return Response(
                    {
                        "error": "Validation failed",
                        "details": {"status": "Status is required."}
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            if new_status not in self.VALID_STATUSES:
                return Response(
                    {
                        "error": "Validation failed",
                        "details": {
                            "status": f'Status must be one of: {", ".join(self.VALID_STATUSES)}'
                        }
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Update task
            result = db.tasks.update_one(
                {"_id": valid_id},
                {"$set": {"status": new_status}}
            )
            
            if result.matched_count == 0:
                raise ResourceNotFound(
                    detail=f"Task with ID '{task_id}' not found."
                )
            
            return Response(
                {
                    "message": "Task status updated successfully",
                    "data": {
                        "task_id": task_id,
                        "status": new_status
                    }
                },
                status=status.HTTP_200_OK
            )
        except InvalidObjectId:
            raise
        except ResourceNotFound:
            raise
        except Exception as e:
            logger.error(f"Error updating task status: {str(e)}")
            raise DatabaseError(detail="Failed to update task status. Please try again.")

class TaskUpdateCreateView(APIView):
    """Handles task updates (comments and progress notes)."""
    
    def get(self, request, task_id):
        """Retrieve all updates for a task."""
        try:
            # Validate task ID format (but don't check if task exists for read operations)
            validate_object_id(task_id, "task_id")
            
            updates = list(db.updates.find({"task_id": task_id}))
            return Response(
                serialize_mongo_doc(updates),
                status=status.HTTP_200_OK
            )
        except InvalidObjectId:
            raise
        except Exception as e:
            logger.error(f"Error fetching task updates: {str(e)}")
            raise DatabaseError(detail="Failed to retrieve task updates. Please try again.")
    
    def post(self, request, task_id):
        """Create a new update for a task."""
        try:
            # Validate task ID
            valid_id = validate_object_id(task_id, "task_id")
            
            # Check if task exists
            task = db.tasks.find_one({"_id": valid_id})
            if not task:
                raise ResourceNotFound(
                    detail=f"Task with ID '{task_id}' not found."
                )
            
            # Prepare payload
            payload = dict(request.data)
            payload["task_id"] = task_id
            
            # Validate update data
            serializer = UpdateSerializer(data=payload)
            if not serializer.is_valid():
                return Response(
                    {
                        "error": "Validation failed",
                        "details": serializer.errors
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Create update
            data = dict(serializer.validated_data)
            result = db.updates.insert_one(data)
            data["_id"] = str(result.inserted_id)
            
            return Response(
                {
                    "message": "Update created successfully",
                    "data": data
                },
                status=status.HTTP_201_CREATED
            )
        except InvalidObjectId:
            raise
        except ResourceNotFound:
            raise
        except Exception as e:
            logger.error(f"Error creating task update: {str(e)}")
            raise DatabaseError(detail="Failed to create task update. Please try again.")
