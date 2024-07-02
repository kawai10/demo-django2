import factory
from django.contrib.auth.hashers import make_password

from src.users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ("email",)

    email = factory.Sequence(lambda n: f"test{n}@test.com")
    name = factory.Faker("name")

    raw_password = factory.Faker("password")

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        raw_password = kwargs.pop("raw_password", None)
        if raw_password:
            kwargs["password"] = make_password(raw_password)

        return super()._create(model_class, *args, **kwargs)
