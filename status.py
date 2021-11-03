from PyInquirer import prompt
import csv

def findindex(name, users):
    res = 0
    for i in users:
        if (i == name):
            return res
        res += 1
    return res

def print_expenses(users, spendings):
    index = 0
    for i in users:
        print(i + " paid: " + str(spendings[index]))
        index += 1

def print_dept(users, spendings):
    print("There should be dept reporting but shit happend")

def status():
    transactions = []
    with open('expense_report.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            transactions.append(row)
    users = []
    
    for i in transactions:
        tmp_list = list(i[3].split(" "))
        for user in tmp_list:
            if user not in users:
                users.append(user)
        if i[2] not in users:
            users.append(i[2])
    spendings = [0] * len(users)
    for i in transactions:
        tmp_list = list(i[3].split(" "))
        tmp_list.append(i[2])
        amount = int(i[0])
        for user in tmp_list:
            index = findindex(user, users)
            spendings[index] += amount / len(tmp_list)
    print_expenses(users, spendings)
    print_dept(users, spendings)
    return True