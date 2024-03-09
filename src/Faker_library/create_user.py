from faker import Faker

fake = Faker(locale="pt-BR")
Faker.seed("Wlisses")


def create_user(name, email):
    return {
        "first_name": name.split()[0],
        "last_name": name.split()[-1],
        "email": email,
        "email_domain": email.split("@")[-1],
    }


if __name__ == "__main__":
    print(create_user(fake.name(), fake.email()))
