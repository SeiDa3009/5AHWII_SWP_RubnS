import random
import sys
import mysql.connector


def mySQL_createDatabase():
    mydb = mysql.connector.connect(host="localhost", user="root", password="htlanich123")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE if not exists rpsls_game")

def mySQL_createTable():
    mydb = mysql.connector.connect(host="localhost", user="root", password="htlanich123", database="rpsls_game")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE if not exists recordedGames (id INT AUTO_INCREMENT PRIMARY KEY, userInput VARCHAR(10), kiInput VARCHAR(10), winner VARCHAR(5))")

def mySQL_insert(uI, kI, uW):
    mydb = mysql.connector.connect(host="localhost", user="root", password="htlanich123", database="rpsls_game")
    mycursor = mydb.cursor()
    sql = "INSERT INTO recordedGames (userInput, kiInput, winner) VALUES (%s, %s, %s)"
    val = (uI, kI, uW)
    mycursor.execute(sql, val)
    mydb.commit()

def mySQL_select_amountGames():
    mydb = mysql.connector.connect(host="localhost", user="root", password="htlanich123", database="rpsls_game")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT count(id) from recordedGames")
    return mycursor.fetchone()[0]

def mySQL_select_amountInput(column, value):
    mydb = mysql.connector.connect(host="localhost", user="root", password="htlanich123", database="rpsls_game")
    mycursor = mydb.cursor()
    mycursor.execute('SELECT count({0}) from recordedGames WHERE {0} = \"{1}\"'.format(column, value))
    return mycursor.fetchone()[0]

if __name__ == "__main__":

    mySQL_createDatabase()
    mySQL_createTable()

    values = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    repeat = True
    user_score = 0
    ki_score = 0
    tie_score = 0

    while (repeat):
        try:
            user_choice = int(input("Rock [0], Paper [1], Scissors [2], Lizard [3], Spock [4]: "))
            user_choice_value = values[user_choice]
        except (ValueError, KeyError, Exception):
            print(user_choice_value)
            print("Lose by default ... no correct input")
            sys.exit(0)

        ki_choice = random.randint(0, 4)
        ki_choice_value = values[ki_choice]

        print("User: " + user_choice_value)
        print("KI: " + ki_choice_value)

        # check who wins
        if ki_choice == user_choice:
            print("Tie!")
            uW = "X"

        elif (user_choice + 1) % 3 == ki_choice:
            print("You lose!")
            uW = "KI"
        else:
            print("You win!")
            uW = "User"

        mySQL_insert(user_choice_value, ki_choice_value, uW)

        repeat_input = input("Play again? [Y/N]: ")
        if repeat_input.upper() == "Y":
            repeat = True
        else:
            repeat = False

        print("Alltime-Summary:")
        print(mySQL_select_amountGames(), "Games")
        print("Rock: ", mySQL_select_amountInput("userInput", "Rock"), "User | ", mySQL_select_amountInput("kiInput", "Rock"),"KI")
        print("Paper: ", mySQL_select_amountInput("userInput", "Paper"), "User | ",mySQL_select_amountInput("kiInput", "Paper"), "KI")
        print("Scissors: ", mySQL_select_amountInput("userInput", "Scissors"), "User | ",mySQL_select_amountInput("kiInput", "Scissors"), "KI")
        print("Lizard: ", mySQL_select_amountInput("userInput", "Lizard"), "User | ",mySQL_select_amountInput("kiInput", "Lizard"), "KI")
        print("Spock: ", mySQL_select_amountInput("userInput", "Spock"), "User | ",mySQL_select_amountInput("kiInput", "Spock"), "KI")

