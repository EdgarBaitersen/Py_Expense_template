from PyInquirer import prompt
import csv

user_questions = [
    {
        "type":"input",
        "name":"UserName",
        "message":"New User - name: ",
    },
]

def add_user():
    infos = prompt(user_questions)
    list = []
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    for i in infos:
        list.append(infos[i])
    with open('users.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(list)
    print("User Added !")
    return True