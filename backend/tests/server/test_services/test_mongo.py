import pytest
from server.services import MongoDB
from mongomock import MongoClient
from server.core import config


# Mock the actual MongoDB with mongomock
@pytest.fixture
def mock_mongo_db(monkeypatch):
    def mock_mongo_client(*args, **kwargs):
        return MongoClient()

    monkeypatch.setattr("server.services.mongo.AsyncIOMotorClient", mock_mongo_client)


@pytest.mark.asyncio
@pytest.mark.usefixtures("mock_mongo_db")
class TestMongoDB:
    @pytest.fixture
    def db(self):
        db = MongoDB()
        db.client = MongoClient(config.MONGO_URI)
        db.db = db.client[config.MONGO_DB]
        return db

    async def test_create_read_document(self, db):
        collection = "test"
        data = {"name": "test_user"}

        # Create Document
        inserted_id = await db.create_document(collection, data)
        assert isinstance(inserted_id, str)

        # Read Document
        read_data = await db.read_document(collection, inserted_id)
        assert read_data == {**data, "_id": inserted_id}

    async def test_update_document(self, db):
        collection = "test"
        data = {"name": "test_user"}

        # Create Document
        inserted_id = await db.create_document(collection, data)

        # Update Document
        new_data = {"name": "updated_user"}
        updated = await db.update_document(collection, inserted_id, new_data)
        assert updated

        # Read Updated Document
        read_data = await db.read_document(collection, inserted_id)
        assert read_data == {**new_data, "_id": inserted_id}

    async def test_delete_document(self, db):
        collection = "test"
        data = {"name": "test_user"}

        # Create Document
        inserted_id = await db.create_document(collection, data)

        # Delete Document
        deleted = await db.delete_document(collection, inserted_id)
        assert deleted

        # Ensure Document No Longer Exists
        read_data = await db.read_document(collection, inserted_id)
        assert read_data is None

    # ... Add more tests as necessary ...
