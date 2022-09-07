import allure
import pytest
import requests
from enums.GlobalEnums import GlobalErrorMessages
from config import BASE_URL
from schemas.models import ResponseHeaders, GetMethodBody, PostMethodBody


@allure.feature('Api-Testing')
@allure.story('GET-method testing')
def test_get_method():
    response = requests.get(f"{BASE_URL}/get")
    print(response.json())
    with allure.step("Запрос отправлен, смотрим код ответа"):
        assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    with allure.step("Валидация заголовков"):
        ResponseHeaders.parse_obj(response.headers)
        GetMethodBody.parse_obj(response.json())


@allure.feature('Api-Testing')
@allure.story('POST-method testing')
def test_post_method():
    response = requests.post(f"{BASE_URL}/post")
    with allure.step("Запрос отправлен, смотрим код ответа"):
        assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    with allure.step("Валидация заголовков"):
        ResponseHeaders.parse_obj(response.headers)
        PostMethodBody.parse_obj(response.json())


@allure.feature('Api-Testing')
@pytest.mark.parametrize("status_code", [200, 300, 400, 500])
@allure.story('Return-status testing')
def test_delete_method(status_code):
    response = requests.post(f"{BASE_URL}/status/{status_code}")
    with allure.step("Запрос отправлен, смотрим код ответа"):
        assert response.status_code == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
    with allure.step("Валидация заголовков"):
        ResponseHeaders.parse_obj(response.headers)
