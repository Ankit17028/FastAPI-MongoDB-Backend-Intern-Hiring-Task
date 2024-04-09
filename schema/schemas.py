def individual_serial(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "name": todo["name"],
        "description": todo["description"],
        "address": todo["address"].dict()
        # "date": todo["date"],
    }

# def individual_serial(todo) -> dict:
#   return {
#     "id": str(todo["_id"]),
#     "name": todo.get("name", ""),  # Add this line here
#     "description": todo["description"],
#     "complete": todo["complete"],
#     # "date": todo["date"],
#   }


def list_serial(todos) -> list:
    return [individual_serial(todo) for todo in todos if "name" in todo]