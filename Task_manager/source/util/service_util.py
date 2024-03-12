from datetime import datetime


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


def sort_id(id, content):
    if len(content) > 0:
        for value in content:
            if value["id"] == id:
                id = int(id) - 1
                break
        return str(id)
    else:
        return id


def time_formatte():
    time = datetime.now().isoformat()
    time_date = time[:10]
    list_date = time_date.split("-")
    formatter_date = f"{list_date[2]}/{list_date[1]}/{list_date[0]}"
    time = time[11:19]
    return f"{formatter_date} {time}"


def prepare_values(title, description, content):
    new_id = sort_id(create_id(content), content)
    return {
        "id": new_id,
        "title": title,
        "description": description,
        "completed": False,
        "creation_date": time_formatte(),
    }


def sort_data_base(content):
    sorted_data_base = sorted(content, key=lambda x: int(x["id"]))
    return sorted_data_base
