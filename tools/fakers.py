import time
from faker import Faker
from faker.providers.python import TEnum


class Fake:
    def __init__(self, faker: Faker):
        self.faker = faker

    def enum(self, value: type[TEnum]) -> TEnum:
        return self.faker.enum(value)

    def category(self) -> str:
        return self.faker.random_element(
            [
                "gas",
                "taxi",
                "tolls",
                "water",
                "beauty",
                "mobile",
                "travel",
                "parking",
                "catalog",
                "internet",
                "satellite",
                "education",
                "government",
                "healthcare",
                "restaurants",
                "electricity",
                "supermarkets",
            ]
        )

    def float(self, start: int = 1, end: int = 100) -> float:
        return self.faker.pyfloat(min_value=start, max_value=end, right_digits=2)

    def amount(self) -> float:

        return self.float(1, 1000)

    def text(self) -> str:
        return self.faker.text()

    def uuid4(self) -> str:
        return self.faker.uuid4()

    def email(self, domain: str | None = None) -> str:
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
