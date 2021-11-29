import json

class JsonGetTestScriptFiles:   
    #read json file class 
    _jsonFileName=""

    #def __init__(self,jsonFileName):
        #self._jsonFileName=jsonFileName
    
    def ReadTestScriptFiles(_jsonFileName,scriptNumber:any):
        # Opening JSON file
        f = open(str(_jsonFileName))
        retList=[]
        # returns JSON object as
        # a dictionary
        data = json.load(f)
        #definitionData=data.get(definition)
        for scriptNum in scriptNumber:
            x=data.get(scriptNumber)
            retList.append(x)
        # Closing file
        f.close()
        return data

    def __del__(self):
      class_name = self.__class__.__name__
    #   print class_name, "destroyed"