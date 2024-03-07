from faker import Faker
from faker.providers import BaseProvider

fake = Faker()

fake = Faker(locale="es-AR")


class MyProvider(BaseProvider):
    def car_license_plate(self) -> str:
        if fake.locales[0].replace("_", "-") == "es-AR":
            ar_first_elements = self.random_element(
                ["AA", "AB", "AC", "AD", "AE"]
            )
            ar_second_elements = self.random_number(4)
            ar_thirth_elements = self.random_element(["ES", "RS", "LS"])
            plate = f"""
{ar_first_elements} {ar_second_elements} {ar_thirth_elements}
            """
            return plate
        elif fake.locales[0].replace("_", "-") == "pt-BR":
            br_first_elements = self.random_element(
                ["AYT", "SAW", "NYG", "PKI"]
            )
            br_second_elements = self.random_element(
                ["7Y45", "2L54", "0N26", "1U20"]
            )
            return f"{br_first_elements}-{br_second_elements}"


fake.add_provider(MyProvider)

print(fake.last_name())
print(fake.email())
print(fake.password())
print(fake.url())
print(fake.text())
print(fake.license_plate())
print(fake.car_license_plate())
