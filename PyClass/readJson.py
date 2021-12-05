import json

class JsonReader:   
    #read json file class 
    _jsonFileName=""

    #def __init__(self,jsonFileName):
        #self._jsonFileName=jsonFileName
    
    def ReadJson(_jsonFileName):
        # Opening JSON file
        f = open(str(_jsonFileName))

        # returns JSON object as
        # a dictionary
        data = json.load(f)

        # Closing file
        f.close()
        return data
    def __del__(self):
      class_name = self.__class__.__name__
    #   print class_name, "destroyed"