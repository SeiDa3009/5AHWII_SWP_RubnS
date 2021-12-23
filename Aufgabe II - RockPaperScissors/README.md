# **Rock, Paper, Scissors, Spock, Lizard - Counter**
##### **Was macht dieses Programm?**
Mit diesem Programm kann das Spiel Rock, Paper, Scissors (mit Spock & Lizard) gespielt werden. 
Während des Spielens zahlt das Programm, wie oft welche Auswahl getroffen wurden.

##### **Was wird dafür benötigt?**
- [My-Sql-Connector](https://www.w3schools.com/python/python_mysql_getstarted.asp)
- [Requests](https://www.w3schools.com/python/module_requests.asp)
- [.exe ausführen](https://gitlab.com/sh1n1xs/rock-paper-scissors-data-server/-/tree/main)


##### **Wie funktioniert das Programm?**
Das Grundprinzip fungiert auf **Rock, Paper, Scissors**. Neben den 3 Auswahlmöglichkeiten gibt es zusätzlich die Möglichkeiten **Spock, Lizard**.
**Nun zum Spielablauf:**
Zuerst sucht sich der Spieler selbst eine von 5 Möglichkeiten (Funktion user_input()). Anschließend wird per Zufallszahl entschieden für welche Auswahl sich der Computer entscheidet.
Nach der Auswahl wird mittels 3 Bedingungen (if, elif, else) ermittelt, wer gewonnen hat (Funktion check_win()). Anschließend wird der Spielende gefragt, ob er erneut spielen wolle (Funktion play_again()).
**Datenbankaufwand im Programm:**
Zuerst wird eine Verbindung zur Datenbank mittels Befehl mysql.connector.connect() erstellt. Weiters wird für die jeweilige Datenbank-Aufgabe eine Funktion geschrieben:
- Erstellen der Datenbank (mySQL_createDatabase())
- Erstellen eines Tables (mySQL_createTable())
- Eingabe der gesammelten Daten über die Auswahlmöglichkeiten (mySQL_insert())
- Für die Ausgabe, die Gesamtanzahl an Spielen die stattgefunden haben (mySQL_select_amountGames())
- Für die Verwertung der Daten in der API eine Select-Statement (mySQL_select_amountInput())
**Push in API:**
Am Ende werden mittels mySQL_select_amountInput()) die Inforamtionen über die Auswahlmöglichkeiten an die API gesendet (sendRequest()).
[Wurde von Schulkollege Mayer aufbereitet](https://gitlab.com/sh1n1xs/rock-paper-scissors-data-server/-/blob/af70e8991db2af704d36bf8caa7f304b10c4cfab/example_request.py)

##### **Ausgeführtes Programm**
![](https://github.com/SeiDa3009/5AHWII_SWP_RubnS/blob/main/Aufgabe%20II%20-%20RockPaperScissors/program_sample.png)

