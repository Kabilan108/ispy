"""
Code for connecting to MongoDB
"""

from typing import Dict, List

from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorDatabase,
)
from bson import ObjectId

from server.core import config


class MongoDB:
    """MongoDB service class."""

    def _str_to_id(self, id: str) -> ObjectId:
        """Convert string to ObjectId."""
        return ObjectId(id)

    def _id_to_str(self, id: ObjectId) -> str:
        """Convert ObjectId to string."""
        return str(id)

    def __init__(self):
        self.client: AsyncIOMotorClient = AsyncIOMotorClient(config.MONGO_URI)
        self.db: AsyncIOMotorDatabase = self.client[config.MONGO_DB]

    async def create_document(
        self, collection: str, data: Dict | List[Dict]
    ) -> str | List[str]:
        """Create document(s) in collection."""

        if isinstance(data, list):
            result = await self.db[collection].insert_many(data)
            return [self._id_to_str(id) for id in result.inserted_ids]
        else:
            result = await self.db[collection].insert_one(data)
            return self._id_to_str(result.inserted_id)

    async def read_document(
        self, collection: str, id: str | List[str]
    ) -> Dict | List[Dict]:
        """Read document(s) from collection by id or list of ids."""

        if isinstance(id, list):
            documents = (
                await self.db[collection]
                .find({"_id": {"$in": [self._str_to_id(i) for i in id]}})
                .to_list(None)
            )
            for document in documents:
                document["_id"] = self._id_to_str(document["_id"])
            return documents
        else:
            document = await self.db[collection].find_one({"_id": self._str_to_id(id)})
            if document:
                document["_id"] = self._id_to_str(document["_id"])
            return document

    async def update_document(
        self, collection: str, id: str | List[str], data: Dict | List[Dict]
    ) -> bool:
        """Update document in collection by id or list of ids."""

        if isinstance(id, list) and isinstance(data, list):
            # Both id and data are lists
            if len(id) != len(data):
                raise ValueError(
                    "When providing lists for both 'id' and 'data', they must have the same length."
                )

            # Update each document with its corresponding data
            for single_id, single_data in zip(id, data):
                result = await self.db[collection].update_one(
                    {"_id": self._str_to_id(single_id)}, {"$set": single_data}
                )
                if result.modified_count == 0:
                    # If one update fails, return False
                    return False
            return True

        elif isinstance(id, str) and isinstance(data, Dict):
            # Single id and data dictionary
            result = await self.db[collection].update_one(
                {"_id": self._str_to_id(id)}, {"$set": data}
            )
            return result.modified_count > 0

        else:
            # Invalid combination of id and data types
            raise TypeError(
                "Invalid combination of 'id' and 'data' types. Ensure you're providing either a single ID with a single data dictionary or lists of IDs with corresponding data dictionaries."
            )

    async def delete_document(self, collection: str, id: str | List[str]) -> bool:
        """Delete document(s) from collection by id or list of ids."""
        if isinstance(id, list):
            result = await self.db[collection].delete_many(
                {"_id": {"$in": [self._str_to_id(i) for i in id]}}
            )
            return result.deleted_count > 0
        else:
            result = await self.db[collection].delete_one({"_id": self._str_to_id(id)})
            return result.deleted_count > 0
