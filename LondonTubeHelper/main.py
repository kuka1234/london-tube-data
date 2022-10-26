import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="test",
  database="londonTube"
)
mycursor = mydb.cursor()

def cleanUp(inputString):
    final = []
    for i in inputString:
        for j in i:
            final.append(j)
    print(final)
    return final
def getStations(name):
    query = "SELECT stations.name FROM stationsLine LEFT JOIN stations ON stationsLine.stationId=stations.id WHERE lineName=%s ORDER BY stationsLine.pos"
    mycursor.execute(query, [name])
    res = cleanUp(mycursor.fetchall())

    return res
def getLines(name):
    query = "SELECT stationsLine.lineName FROM stationsLine LEFT JOIN stations ON stationsLine.stationId=stations.id WHERE name=%s"
    mycursor.execute(query, [name])
    res = cleanUp(mycursor.fetchall())
    return res

def askForLine():
    while True:
        line = input("Please enter the line or type back to go back: ")
        if line == "back":
            return
        else:
            stations = getStations(line)
            if stations == None:
                print("Line you have entered are not valid.")

def askForStation():
    while True:
        station = input("Please enter the station or type back to go back: ")
        if station == "back":
            return
        else:
            lines = getLines(station)
            if lines == None:
                print("Station you have entered are not valid.")

def askForInput():
    while True:
        userInput = input("Press 1 to get stations on each line or Press 2 to get lines for each station: ")
        if userInput == "1":
            askForLine()
        elif userInput == "2":
            askForStation()
        else:
            "Input not valid."
askForInput()