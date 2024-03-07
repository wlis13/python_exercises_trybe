from faker import Faker
from faker.providers import BaseProvider
from data_values import dates_locales

fake = Faker()

fake = Faker(locale="en-US")


class MyProvider(BaseProvider):
    def car_license_plate(self) -> str:
        for key in dates_locales.keys():
            if fake.locales[0].replace("_", "-") == key:
                if "half_part" in dates_locales[key]:

                    first_element = dates_locales[key]["first_part"]
                    half_element = dates_locales[key]["half_part"]
                    second_element = dates_locales[key]["second_part"]

                    return f"{first_element} {half_element} {second_element}"
                else:
                    first_element = dates_locales[key]["first_part"]
                    second_element = dates_locales[key]["second_part"]
                    if dates_locales[key] == "en-US":
                        return f"{first_element}{second_element}"
                    else:
                        return f"{first_element}-{second_element}"


fake.add_provider(MyProvider)

print(fake.last_name())
print(fake.email())
print(fake.password())
print(fake.url())
print(fake.car_license_plate())
