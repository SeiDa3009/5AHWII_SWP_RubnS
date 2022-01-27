import random
import sys
import mysql.connector
import requests


def mySQL_createDatabase():
    mydb = mysql.connector.connect(host="localhost", user="root", password="root")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE if not exists rpsls_game")

def mySQL_createTable():
    mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="rpsls_game")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE if not exists recordedGames (id INT AUTO_INCREMENT PRIMARY KEY, userInput VARCHAR(10), kiInput VARCHAR(10), winner VARCHAR(5))")

def mySQL_insert(uI, kI, uW):
    mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="rpsls_game")
    mycursor = mydb.cursor()
    sql = "INSERT INTO recordedGames (userInput, kiInput, winner) VALUES (%s, %s, %s)"
    val = (uI, kI, uW)
    mycursor.execute(sql, val)
    mydb.commit()

def mySQL_select_amountGames():
    mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="rpsls_game")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT count(id) from recordedGames")
    return mycursor.fetchone()[0]

def mySQL_select_amountInput(column, value):
    mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="rpsls_game")
    mycursor = mydb.cursor()
    mycursor.execute('SELECT count({0}) from recordedGames WHERE {0} = \"{1}\"'.format(column, value))
    return mycursor.fetchone()[0]

def play_again():
    repeat_input = input("Play again? [Y/N]: ")
    if repeat_input.upper() == "Y":
        return True
    else:
        return False

def sendRequest(username, countScissors, countRock, countPaper, countSpock, countLizard, apiIP="http://127.0.0.1:5000"):
    reqUrl = apiIP + "/v1/updateRecord"
    reqUrl += "?username=" + str(username) + "&voteScissors=" + str(countScissors)
    reqUrl += "&voteRock=" + str(countRock) + "&votePaper=" + str(countPaper)
    reqUrl += "&voteSpock=" + str(countSpock) + "&voteLizard=" + str(countLizard)
    responseCode = 0
    try:
        response = requests.post(reqUrl, None)
        responseCode = response.status_code
    except:
        return 0
    return responseCode

def user_input():
    try:
        user_choice = int(input("Rock [0], Paper [1], Scissors [2], Lizard [3], Spock [4]: "))
        return user_choice
    except (ValueError, KeyError, Exception):
        print(user_choice_value)
        print("Lose by default ... no correct input")
        sys.exit(0)

def check_win(user_choice, ki_choice, user_choice_value, ki_choice_value):
    print("User: " + user_choice_value)
    print("KI: " + ki_choice_value)

    # check who wins
    if ki_choice == user_choice:
        print("Tie!")
        return "X"

    elif (user_choice + 1) % 3 == ki_choice:
        print("You lose!")
        return "KI"
    else:
        print("You win!")
        return "User"

def output():
    print("Alltime-Summary:")
    print(mySQL_select_amountGames(), "Games")
    print("Scissors: ", mySQL_select_amountInput("userInput", "Scissors"), "User | ",
          mySQL_select_amountInput("kiInput", "Scissors"), "KI")
    print("Rock: ", mySQL_select_amountInput("userInput", "Rock"), "User | ",
          mySQL_select_amountInput("kiInput", "Rock"), "KI")
    print("Paper: ", mySQL_select_amountInput("userInput", "Paper"), "User | ",
          mySQL_select_amountInput("kiInput", "Paper"), "KI")
    print("Spock: ", mySQL_select_amountInput("userInput", "Spock"), "User | ",
          mySQL_select_amountInput("kiInput", "Spock"), "KI")
    print("Lizard: ", mySQL_select_amountInput("userInput", "Lizard"), "User | ",
          mySQL_select_amountInput("kiInput", "Lizard"), "KI")

def get_summary_data(user_input, ki_input, value):
    sum = 0
    sum = mySQL_select_amountInput(user_input, value) + mySQL_select_amountInput(ki_input, value)
    return sum

def send_request():
    return sendRequest("SeiDa", get_summary_data("userInput", "kiInput", "Scissors"), get_summary_data("userInput", "kiInput", "Rock"), get_summary_data("userInput", "kiInput", "Paper"), get_summary_data("userInput", "kiInput", "Spock"), get_summary_data("userInput", "kiInput", "Lizard"))

if __name__ == "__main__":
    values = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    repeat = True

    mySQL_createDatabase()
    mySQL_createTable()
    while (repeat):
        user_choice = user_input()
        user_choice_value = values[user_choice]


        ki_choice = random.randint(0, 4)
        ki_choice_value = values[ki_choice]

        mySQL_insert(user_choice_value, ki_choice_value, check_win(user_choice,ki_choice,user_choice_value,ki_choice_value))

        repeat = play_again()

    output()

    print("sending test request")
    code = send_request()
    print("Done")
    print("code=" + str(code))



