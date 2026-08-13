import sys
import os
import shutil

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import app
import database
import pytest


@pytest.fixture
def client():

    if os.path.exists("test_canteen.db"):
        os.remove("test_canteen.db")

    database.DATABASE = "test_canteen.db"

    database.initialize_database()

    app.app.config["TESTING"] = True

    yield app.app.test_client()

    if os.path.exists("test_canteen.db"):
        os.remove("test_canteen.db")

    database.DATABASE = "canteen.db"


def test_home_page(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"Burger" in response.data


def test_successful_order(client):
    response = client.post(
        "/order",
        data={
            "food_id": "1",
            "quantity": "2"
        }
    )

    assert response.status_code == 200
    assert b"Order Successful" in response.data
    assert b"160" in response.data
    assert b"8" in response.data


def test_zero_quantity(client):
    response = client.post(
        "/order",
        data={
            "food_id": "1",
            "quantity": "0"
        }
    )

    assert response.status_code == 400


def test_insufficient_stock(client):
    response = client.post(
        "/order",
        data={
            "food_id": "1",
            "quantity": "100"
        }
    )

    assert response.status_code == 400
def test_maximum_quantity(client):
    response = client.post(
        "/order",
        data={
            "food_id": "1",
            "quantity": "11"
        }
    )

    assert response.status_code == 400
    