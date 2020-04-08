import shelve

locations = shelve.open("locations")

locations['0'] = {"desc": "You are sitting infront of the computer learning python.",
                  "exists": {},
                  "namedExists": {}}

locations['1'] = {"desc": "You are standing at the end of the road before a small brick building.",
                  "exists": {"W": '2', "E": '3', "N": '5', "S": '4', "Q": '0'},
                  "namedExists": {"2": '2', "3": '3', "5": '5', "4": '4'}}


locations['2'] = {"desc": "You are at the top of hill.",
                  "exists": {"N": '5', "Q": '0'},
                  "namedExists": {"5": '5'}}

locations['3'] = {"desc": "You are inside the building, a well house for a small stream.",
                  "exists": {"W": '1', "Q": '0'},
                  "namedExists": {"1": '1'}}

locations['4'] = {"desc": "You are in a valley beside a stream.",
                  "exists": {"N": '1', "W": '2', "Q": '0'},
                  "namedExists": {"1": '1', "2": '2'}}

locations['5'] = {"desc": "You are in the forest.",
                  "exists": {"W": '2', "S": '1',  "Q": '0'},
                  "namedExists": {"2": '2', "1": '1'}}

locations.close()

vocabulary = shelve.open("vocabulary")

vocabulary["QUIT"] = "Q"
vocabulary["NORTH"] = "N"
vocabulary["SOUTH"] = "S"
vocabulary["EAST"] = "E"
vocabulary["WEST"] = "W"
vocabulary["ROAD"] = "1"
vocabulary["HILL"] = "2"
vocabulary["BUILDING"] = "3"
vocabulary["VALLEY"] = "4"
vocabulary["FOREST"] = "5"

vocabulary.close()
