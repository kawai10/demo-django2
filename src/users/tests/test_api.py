import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APIClient
from src.users.models import User
from src.users.tests.factories import UserFactory


def create_user(raw_password: str) -> User:
    return UserFactory(raw_password=raw_password)


@pytest.fixture
def unauthenticated_api_client() -> APIClient:
    return APIClient()


@pytest.fixture
def api_client_with_force_auth(faker) -> APIClient:
    user = create_user(raw_password=faker.password(length=12))
    client = APIClient()
    client.force_authenticate(user)
    return client


@pytest.mark.it("유저 회원가입 API 테스트")
@pytest.mark.django_db
def test_signup(unauthenticated_api_client, faker):
    data = {
        "email": faker.email(),
        "password": faker.password(length=12),
        "name": faker.name(),
    }

    url: str = reverse("users:user-signup")
    response: Response = unauthenticated_api_client.post(url, data=data, format="json")
    assert status.HTTP_201_CREATED == response.status_code


@pytest.mark.it("유저 로그인 테스트")
@pytest.mark.django_db
# 유저 생성시에 패스워드를 암호화해서 저장해야함.
# 로그인 API post 시에는 암호화 되기전의 패스워드를 넣어야함.
def test_login(unauthenticated_api_client, faker):
    password = faker.password(length=12)

    user: User = create_user(raw_password=password)
    data = {"email": user.email, "password": password}

    url: str = reverse("users:user-login")
    response: Response = unauthenticated_api_client.post(url, data=data)

    assert response.status_code == status.HTTP_200_OK


@pytest.mark.it("모든 유저 조회")
@pytest.mark.django_db
def test_get_all_users(api_client_with_force_auth):
    user_list = [UserFactory() for __ in range(10)]
    url: str = reverse("users:user-list")
    response: Response = api_client_with_force_auth.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == len(user_list) + 1
