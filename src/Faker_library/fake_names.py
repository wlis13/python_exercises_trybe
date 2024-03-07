from faker import Faker
from faker.providers import BaseProvider
from data_values import dates

fake = Faker()

fake = Faker(locale="es-AR")


class MyProvider(BaseProvider):
    def car_license_plate(self) -> str:
        for key in dates.keys():
            if fake.locales[0].replace("_", "-") == key:
                if "half_part" in dates[key]:

                    first_element = dates[key]["first_part"]
                    half_element = dates[key]["half_part"]
                    second_element = dates[key]["second_part"]

                    return f"{first_element} {half_element} {second_element}"
                else:
                    first_element = dates[key]["first_part"]
                    second_element = dates[key]["second_part"]

                    return f"{first_element}-{second_element}"


fake.add_provider(MyProvider)

print(fake.last_name())
print(fake.email())
print(fake.password())
print(fake.url())
print(fake.car_license_plate())
