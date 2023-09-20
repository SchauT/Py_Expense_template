from PyInquirer import prompt, print_json
import csv

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New User - Name: ",
    },
]

def add_user():
    # This function should create a new user, asking for its name
    infos = prompt(user_questions)

    # Reading if user already exists
    with open('users.csv', 'r', newline='') as f:
        # read lines and check if user already exists
        reader = csv.reader(f)
        for row in reader:
            if row[0] == infos['name']:
                print("User already exists !")
                return

    # Writing the informations on external file
    with open('users.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        infos['debt'] = 0
        writer.writerows([infos.values()])

    print(infos['name'] + " added !")
    return

def get_users():
    users = []

    with open('users.csv', 'r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            users.append({"name": row[0], "checked": False}) #, "debt": row[1]})

    return users
