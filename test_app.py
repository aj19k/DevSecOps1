from app import app


def test_home_status_code() -> None:
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_home_response_text() -> None:
    client = app.test_client()
    response = client.get("/")
    assert response.data.decode("utf-8") == "Hello from Python + Docker!"


def test_unknown_route_returns_404() -> None:
    client = app.test_client()
    response = client.get("/does-not-exist")
    assert response.status_code == 404