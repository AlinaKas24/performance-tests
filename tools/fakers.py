import time
from faker import Faker


class Fake:
    def __init__(self, faker: Faker):
        self.faker = faker

    def text(self) -> str:
        return self.faker.text()

    def uuid4(self) -> str:
        return self.faker.uuid4()

    def email(self, domain: str | None = None) -> str:
        """
        Генерирует случайный email.

        :param domain: Домен электронной почты (например, "example.com").
        Если не указан, будет использован случайный домен.
        :return: Случайный email.
        """
        return self.faker.email(domain=domain)

    def description(self) -> str:
        return self.faker.sentence()

    def password(self) -> str:
        return self.faker.password()

    def last_name(self) -> str:
        return self.faker.last_name()

    def first_name(self) -> str:
        return self.faker.first_name()

    def middle_name(self) -> str:
        return self.faker.middle_name()

    def phone_number(self) -> str:
        return self.faker.phone_number()

    def integer(self, start: int = 1, end: int = 100) -> int:
        return self.faker.random_int(start, end)


fake = Fake(faker=Faker())
