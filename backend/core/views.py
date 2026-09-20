from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .mongo import db
from bson import ObjectId

class EmployeeListCreateView(APIView):
    def get(self, request):
        employees = list(db.employees.find())
        for e in employees:
            e["_id"] = str(e["_id"])  # ObjectId isn't JSON-serializable by default
        return Response(employees)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            data = dict(serializer.validated_data)  # make a copy first
            result = db.employees.insert_one(data)
            data["_id"] = str(result.inserted_id)   # now safely stringify it
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskListCreateView(APIView):
    def get(self, request):
        tasks = list(db.tasks.find())
        for t in tasks:
            t["_id"] = str(t["_id"])
        return Response(tasks)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            data = dict(serializer.validated_data)
            result = db.tasks.insert_one(data)
            data["_id"] = str(result.inserted_id)
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskStatusUpdateView(APIView):
    def patch(self, request, task_id):
        new_status = request.data.get("status")
        if new_status not in ["working", "paused", "stopped"]:
            return Response({"error": "invalid status"}, status=status.HTTP_400_BAD_REQUEST)
        db.tasks.update_one({"_id": ObjectId(task_id)}, {"$set": {"status": new_status}})
        return Response({"task_id": task_id, "status": new_status})


class TaskUpdateCreateView(APIView):
    def get(self, request, task_id):
        updates = list(db.updates.find({"task_id": task_id}))
        for u in updates:
            u["_id"] = str(u["_id"])
        return Response(updates)

    def post(self, request, task_id):
        payload = dict(request.data)
        payload["task_id"] = task_id
        serializer = UpdateSerializer(data=payload)
        if serializer.is_valid():
            data = dict(serializer.validated_data)
            result = db.updates.insert_one(data)
            data["_id"] = str(result.inserted_id)
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)