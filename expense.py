from PyInquirer import prompt
import csv

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
        "type":"input",
        "name":"spender",
        "message":"New Expense - Spender: ",
    },
    {
        "type":"input",
        "name":"people",
        "message":"New Expense - People involved: ",
    },

]

def check_spender(name):
    list = []
    with open('users.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if (row[0] == name):
                return True
    return False

def new_expense(*args):
    infos = prompt(expense_questions)
    list_csv = []
    for i in infos:
        if ((i == "spender")and check_spender(infos[i]) == False):
            print("The spender is not a user !")
            return False
        if (i == "people"):
            tmp_list = list(infos[i].split(" "))
            for user in tmp_list:
                if (check_spender(user) == False):
                    print("One of the users to split the bill with does not exist")
                    return False
        list_csv.append(infos[i])
    with open('expense_report.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(list_csv)
    print("Expense Added !")
    return True


