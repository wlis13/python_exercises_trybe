from ...src.Faker_library.create_user import create_user
from ...src.Faker_library.generate_user_date import generate_user_data
from faker import Faker


def test_faker_email(faker):
    faker_email = faker.email()
    assert isinstance(faker_email, str)
    assert "@" in faker_email
    assert "." in faker_email
    assert type(faker_email) is str


def test_generate_user_data(faker):
    name = faker.name()
    email = faker.email()
    phone = faker.phone_number()

    result = generate_user_data(name, email, phone)

    assert result["Name"] == name
    assert result["Email"] == email
    assert result["Phone"] == f"+55 {phone}"


def test_create_user():
    fake = Faker(locale="pt-BR")
    Faker.seed("Wlisses")
    name = fake.name()
    email = fake.email()

    result = create_user(name, email)
    assert name.startswith(result["first_name"])
    assert name.endswith(result["last_name"])
    assert email is result["email"]
    assert email.endswith(result["email_domain"])
