from requests import get
import time
import json

class Main:
    def __init__():
        file = get("https://services.marinetraffic.com/api/exportvessels/v:8/2bede1ff947de189f635a8781c0d606b455f61b4/timespan:2/protocol:json")
        file = "SampleData_4_9__10-09am.txt" # Sample data; not sure if syntax is correct
        jsonObj = json.loads(file.text)
        jsonObj = file

        self.currentShips = Ships(jsonObj)
        self.Ahmet = Ahmet(40, 40) # Arbitrary

        pastShips = []

while true:
    # Phase 1: Data gathering
    mainRunner = Main()

    # Phase 2A: Base filter of ships within radius
    shipsWithinRadius = DataProcessing.withinRadiusShips(mainRunner.currentShips.allShips, mainRunner.currentAhmet)
    print(shipsWithinRadius)

    # Phase 2B: Direction filter
    shipsDirectionTuple = DataProcessing.withinDirectionShips(shipsWithinRadius, ahmet)
    shipsTowards = shipsDirectionTuple[0]
    shipsAway = shipsDirectionTuple[1]
    print(shipsTowards, shipsAway)

    # Phase 3: Alert Ahmet if he presses the button


    # REPEAT: Delay for 5 minutes
    time.sleep(300)

# predicting header for the ships
# keep track of past ships
# testing
