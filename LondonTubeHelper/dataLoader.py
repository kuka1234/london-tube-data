import mysql.connector
import json

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="test",
  database="londonTube"
)

mycursor = mydb.cursor()
#

# # Opening JSON file

f = open("C:/Users/shree\PycharmProjects/vaticleInterview/london-tube-data/train-network.json")
data = json.load(f)

def loadStations(data):
  for i in data['stations']:
    stationId = i["id"]
    stationName = i["name"]
    stationLong = i["longitude"]
    stationLat = i["latitude"]
    query = "INSERT INTO stations VALUES(%s, %s, %s, %s);"
    mycursor.execute(query, (stationId,stationName,stationLong,stationLat))
    mydb.commit()



def makeStationsToLineTable(data):
  stationToLine = []
  for i in data['lines']:
    j = 0
    for station in i["stations"]:
      stationToLine.append((station,i["name"], j))
      j += 1


  for station,line,pos in stationToLine:
    stationId = station
    lineName = line
    pos = pos
    query = "INSERT INTO stationsLine VALUES(%s, %s, %s);"
    mycursor.execute(query, (stationId,lineName,pos))
    mydb.commit()
# loadStations(data)
# makeStationsToLineTable(data)

f.close()
mycursor.execute("SELECT * FROM stations")