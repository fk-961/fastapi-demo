import json

def create_expenses() -> None:
    """Creates the JSON file containing our initial dataset.
    """
    data = []
    users = ["John", "Yuri", "Harry"]
    for i in range(1,6):
        data.append(
            {
                "amount" : i*10,
                "category" : "food",
                "user" : users[i%3-1]
            }
        )
        data.append(
            {
                "amount" : i*10+5,
                "category" : "transport",
                "user" : users[i%3-1]
            }
        )
        data.append(
            {
                "amount" : i%10+2,
                "category" : "drinks",
                "user" : users[i%3-1]
            }
        )
        
        with open("./expenses.json", "w") as f:
            json.dump(data, f)
            
if __name__ == "__main__":
    create_expenses()