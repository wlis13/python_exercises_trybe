from ...src.Faker_library.generate_user_date import generate_user_data


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
