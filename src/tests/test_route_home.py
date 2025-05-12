from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_route_home():
    response = client.get("/api/v1/test")
    print(response.text)
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Word!"}


def test_route_index():
    response = client.get("/api/v1/")
    print(response.text)
    assert response.status_code == 200
    assert response.json() == {"msg": "This endpoint has no limits."}


def test_route_search_handler():
    response = client.get("/api/v1/search")
    print(response.text)
    assert response.status_code == 200
    assert response.json() == {"msg": "This endpoint has a rate limit of 2 requests per 5 seconds."}


def test_route_upload_handler():
    response = client.get("/api/v1/upload")
    print(response.text)
    assert response.status_code == 200
    assert response.json() == {"msg": "This endpoint has a rate limit of 2 requests per 10 seconds."}


def test_get_items_default():
    response = client.get("/api/v1/items/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 10  # padrão limit=10
    assert data[0]["item_id"] == 1


def test_get_items_skip_limit():
    response = client.get("/api/v1/items/?skip=10&limit=5")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 5
    assert data[0]["item_id"] == 11