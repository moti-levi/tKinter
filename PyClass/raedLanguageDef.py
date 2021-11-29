import json

class JsonDefinitionLanguage:   
    #read json file class 
    _jsonFileName=""

    #def __init__(self,jsonFileName):
        #self._jsonFileName=jsonFileName
    
    def ReadJsonLanguage(_jsonFileName,definition:str):
        # Opening JSON file
        f = open(str(_jsonFileName))

        # returns JSON object as
        # a dictionary
        data = json.load(f)
        definitionData=data.get(definition)
        # Closing file
        f.close()
        return data[definition]
    def __del__(self):
      class_name = self.__class__.__name__
    #   print class_name, "destroyed"