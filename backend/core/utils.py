"""
Utility functions for validation and database operations.
"""
from bson import ObjectId
from bson.errors import InvalidId
from .exceptions import InvalidObjectId

def validate_object_id(obj_id, field_name="ID"):
    """
    Validate if a string is a valid MongoDB ObjectId.
    
    Args:
        obj_id: The ID string to validate
        field_name: Name of the field for error messages
        
    Returns:
        ObjectId: Valid ObjectId instance
        
    Raises:
        InvalidObjectId: If the ID is invalid
    """
    try:
        return ObjectId(obj_id)
    except (InvalidId, TypeError):
        raise InvalidObjectId(
            detail=f"Invalid {field_name}. Must be a valid MongoDB ObjectId."
        )

def serialize_mongo_doc(doc):
    """
    Convert MongoDB document to JSON-serializable format.
    Converts ObjectId to string.
    
    Args:
        doc: MongoDB document
        
    Returns:
        dict: Document with ObjectId converted to string
    """
    if doc is None:
        return None
    if isinstance(doc, list):
        return [serialize_mongo_doc(d) for d in doc]
    if isinstance(doc, dict):
        doc_copy = doc.copy()
        if "_id" in doc_copy:
            doc_copy["_id"] = str(doc_copy["_id"])
        return doc_copy
    return doc
