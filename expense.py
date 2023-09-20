from PyInquirer import prompt
import csv
from user import get_users

users = []

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": users
    },

]

expense_questions_shared = [
    {
        "type":"checkbox",
        "name":"shared",
        "message":"New Expense - Shared: ",
        "choices": users
    },
]

def new_expense(*args):
    users = get_users()
    print(users)

    infos = prompt(expense_questions)

    for user in users:
        if user['name'] == infos['spender']:
            user['checked'] = True


    sharing_infos = prompt(expense_questions_shared)

    infos_list = list(infos.values())
    sharing_infos_list = list(sharing_infos.values())
    with open('expense_report.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerows([infos_list + sharing_infos_list])

    with open('users.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for user in users:
            if sharing_infos_list.contains(user['name']):
                user['debt'] = int(user['debt']) + int(infos['amount']) / len(sharing_infos_list)
            writer.writerows([[user['name'], user['debt']]])

    print("Expense Added !")
    return True

def get_status():
    users = get_users()

    for user in users:
        print("- " + user['name'] + " : " + str(user['debt']))

    return
