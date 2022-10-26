
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
            lines = getLine(station)
            if lines == None:
                print("Line you have entered are not valid.")

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