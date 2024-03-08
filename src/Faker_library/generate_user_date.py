def generate_user_data(name, email, phone) -> str:
    name = name.title()
    phone = f"+55 {phone}"

    return {"Name": name, "Email": email, "Phone": phone}


if __name__ == "__main__":
    name = "wlisses"
    email = "wlisses@gmail.com"
    phone = "3176458214"

    print(generate_user_data(name, email, phone))
