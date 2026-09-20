try:
    from pymongo import MongoClient
except ImportError:  # pragma: no cover
    MongoClient = None  # type: ignore[assignment]

from django.conf import settings

if MongoClient is not None:
    client = MongoClient(settings.MONGO_URI)
    db = client["micromanage_db"]
else:
    client = None
    db = None
