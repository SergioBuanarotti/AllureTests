import pytest
import requests
from enums.GlobalEnums import GlobalErrorMessages
from config import BASE_URL
from schemas.models import ResponseHeaders, GetMethodBody, PostMethodBody


def test_get_method():
    response = requests.get(f"{BASE_URL}/get")
    print(response.json())
    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    ResponseHeaders.parse_obj(response.headers)
    GetMethodBody.parse_obj(response.json())


def test_post_method():
    response = requests.post(f"{BASE_URL}/post")
    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    ResponseHeaders.parse_obj(response.headers)
    PostMethodBody.parse_obj(response.json())


@pytest.mark.parametrize("status_code", [200, 300, 400, 500])
def test_delete_method(status_code):
    response = requests.post(f"{BASE_URL}/status/{status_code}")
    assert response.status_code == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
    ResponseHeaders.parse_obj(response.headers)
