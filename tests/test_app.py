
from app import app


def test_homepage():
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.get("/")

        assert response.status_code == 200
        assert response.json["status"] == "success"


def test_health():
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.get("/health")

        assert response.status_code == 200
        assert response.json["status"] == "healthy"
