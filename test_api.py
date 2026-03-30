import requests
import random

BASE_URL = "https://qa-internship.avito.com/api/1"


def test_create_and_get_item():
    # уникальный sellerId
    seller_id = random.randint(100000, 999999)

    payload = {
        "sellerId": seller_id,
        "name": "Test item",
        "price": 1000,
        "statistics": {
            "likes": 1,
            "viewCount": 1,
            "contacts": 1
        }
    }

    # создаём объявление
    response = requests.post(f"{BASE_URL}/item", json=payload)
    assert response.status_code == 200

    data = response.json()
    assert "status" in data

    item_id = data["status"].split(" - ")[1]

    # получаем объявление
    get_response = requests.get(f"{BASE_URL}/item/{item_id}")
    assert get_response.status_code == 200

    items = get_response.json()
    assert isinstance(items, list)
    assert len(items) > 0

    item = items[0]

    # проверка структуры ответа
    assert "id" in item
    assert "name" in item
    assert "price" in item
    assert "sellerId" in item
    assert "statistics" in item

    # проверки данных
    assert item["name"] == payload["name"]
    assert item["price"] == payload["price"]
    assert item["sellerId"] == payload["sellerId"]


def test_get_item_with_invalid_id():
    response = requests.get(f"{BASE_URL}/item/1")

    assert response.status_code == 400

    data = response.json()
    assert "result" in data
    assert "message" in data["result"]
    assert "UUID" in data["result"]["message"]


def test_get_items_by_seller_id():
    seller_id = random.randint(100000, 999999)

    payload = {
        "sellerId": seller_id,
        "name": "Seller item",
        "price": 2000,
        "statistics": {
            "likes": 2,
            "viewCount": 3,
            "contacts": 4
        }
    }

    create_response = requests.post(f"{BASE_URL}/item", json=payload)
    assert create_response.status_code == 200

    response = requests.get(f"{BASE_URL}/{seller_id}/item")
    assert response.status_code == 200

    items = response.json()
    assert isinstance(items, list)
    assert len(items) > 0

    found = False
    for item in items:
        if item["sellerId"] == seller_id and item["name"] == payload["name"]:
            found = True
            break

    assert found


def test_get_statistics_by_item_id():
    seller_id = random.randint(111111, 999999)

    payload = {
        "sellerId": seller_id,
        "name": "Statistics item",
        "price": 3000,
        "statistics": {
            "likes": 5,
            "viewCount": 15,
            "contacts": 3
        }
    }

    create_response = requests.post(f"{BASE_URL}/item", json=payload)
    assert create_response.status_code == 200

    create_data = create_response.json()
    item_id = create_data["status"].split(" - ")[1]

    response = requests.get(f"{BASE_URL}/statistic/{item_id}")
    assert response.status_code == 200

    stats = response.json()
    assert isinstance(stats, list)
    assert len(stats) > 0

    stat = stats[0]

    assert "likes" in stat
    assert "viewCount" in stat
    assert "contacts" in stat

    assert stat["likes"] == payload["statistics"]["likes"]
    assert stat["viewCount"] == payload["statistics"]["viewCount"]
    assert stat["contacts"] == payload["statistics"]["contacts"]

