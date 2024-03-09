def remove_zero(id):
    if int(id) < 10 and len(id) < 2:
        return f"0{id}"
    else:
        return id


def create_id(content):
    if len(content) < 10:
        id_value = f"0{int(len(content)) + 1}"
    else:
        id_value = f"{int(len(content)) + 1}"

    return id_value


def added_zero(id):
    if int(id) < 10:
        id_value = f"0{id}"
    else:
        id_value = f"{id}"

    return id_value


def sort_id(id, content):
    if len(content) > 0:
        for value in content:
            if value["id"] == id:
                id = int(id) - 1
                break
        return added_zero(id)


def prepare_values(title, description, content):
    new_id = sort_id(create_id(content), content)
    return {
        "id": new_id,
        "title": title,
        "description": description,
    }


def sort_data_base(content):
    sorted_data_base = sorted(content, key=lambda x: int(x["id"]))
    return sorted_data_base
