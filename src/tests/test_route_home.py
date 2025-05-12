from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_item():
    response = client.get("/api/v1/test")
    print(response.text)
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Word!"}



