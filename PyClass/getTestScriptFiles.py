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
            scriptFiles=data.get(str(scriptNum)).get('PC scripts')
            for scriptFile in scriptFiles:
                retList.append(scriptFile)
        # Closing file
        f.close()
        return retList

    def ReadTestScriptFilesRunTime(_jsonFileName,scriptNumber:any):
        # Opening JSON file
        f = open(str(_jsonFileName))
        retTime:int=0
        # returns JSON object as
        # a dictionary
        data = json.load(f)
        #definitionData=data.get(definition)
        for scriptNum in scriptNumber:
            scriptFilesTime=data.get(str(scriptNum)).get('Time')            
            retTime+=int(scriptFilesTime)
        # Closing file
        f.close()
        return retTime

    def __del__(self):
      class_name = self.__class__.__name__
    #   print class_name, "destroyed"