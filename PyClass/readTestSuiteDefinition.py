import json

class JsonDefinitionReader:   
    #read json file class 
    _jsonFileName=""

    #def __init__(self,jsonFileName):
        #self._jsonFileName=jsonFileName
    
    def ReadJsonDefinition(_jsonFileName,definition:str):
        # Opening JSON file
        f = open(str(_jsonFileName))
        retdict={}        
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