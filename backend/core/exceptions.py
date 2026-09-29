"""
Custom exception classes for structured error handling.
"""
from rest_framework.exceptions import APIException
from rest_framework import status

class InvalidObjectId(APIException):
    """Raised when an invalid MongoDB ObjectId is provided."""
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Invalid ID format. Must be a valid MongoDB ObjectId."
    default_code = "invalid_object_id"

class ResourceNotFound(APIException):
    """Raised when a resource is not found."""
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "The requested resource was not found."
    default_code = "not_found"

class DatabaseError(APIException):
    """Raised when a database operation fails."""
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = "A database error occurred. Please try again later."
    default_code = "database_error"

class ValidationError(APIException):
    """Raised when input validation fails."""
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = "invalid_input"
