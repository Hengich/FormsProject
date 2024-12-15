import pytest
import requests

BASE_URL = "http://localhost:8000/get_form/"


@pytest.mark.parametrize("input_data,expected_output", [
    # Тест: Полная форма соответствует "Contact Form"
    ({"user_email": "email@example.com", "user_phone": "+7 123 456 78 90"}, {"template_name": "Contact Form"}),
    # Тест: Полная форма соответствует "Order Form"
    ({"order_email": "email@example.com", "order_phone": "+7 123 456 78 90", "order_date": "2024-12-13"}, {"template_name": "Order Form"}),
    # Тест: Частичное совпадение полей с "Order Form"
    ({"order_email": "email@example.com", "order_phone": "+7 123 456 78 90"}, {
        "order_email": "email",
        "order_phone": "phone"
    }),
    # Тест: Неверные данные
    ({"user_email": "invalid_email", "user_phone": "not_a_phone"}, {
        "user_email": "text",
        "user_phone": "text"
    }),
    # Тест: Некорректный email
    ({"user_email": "invalid_email", "user_phone": "+7 123 456 78 90"}, {
        "user_email": "text",
        "user_phone": "phone"
    }),
    # Тест: Некорректный телефон
    ({"user_email": "example@example.com", "user_phone": "not_a_phone"}, {
        "user_email": "email",
        "user_phone": "text"
    }),
    # Тест: Некорректная дата
    ({"order_date": "13-12-2024", "order_email": "valid@example.com"}, {
        "order_date": "text",
        "order_email": "email"
    }),
    # Тест: Дополнительное поле, которого нет в шаблонах
    ({"user_email": "email@example.com", "user_phone": "+7 123 456 78 90", "extra_field": "some_value"}, {
        "template_name": "Contact Form"
    }),
])
def test_get_form(input_data, expected_output):
    """
    Тесты для проверки API /get_form.
    """
    response = requests.post(BASE_URL, data=input_data)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    assert response.json() == expected_output, f"Unexpected response: {response.json()}"
