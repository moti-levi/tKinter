import json

class JsonDefinitionLanguage:   
    #read json file class 
    _jsonFileName=""

    #def __init__(self,jsonFileName):
        #self._jsonFileName=jsonFileName
    
    def ReadJsonLanguage(_jsonFileName,definitionLang:str):
        # Opening JSON file
        f = open(str(_jsonFileName))
         # returns JSON object as
        # a dictionary
        RetDict={}
        with open('Lang\Language_definitions.json', encoding="utf-8") as f:
            data = json.load(f)
            # print(data)
       
        # data = json.load(f)                
        for i in data.get(definitionLang)['Test Suites']:
            RetDict[i]=data.get(definitionLang)['Test Suites'][i]
        # Closing file
        f.close()
        return RetDict
    def __del__(self):
      class_name = self.__class__.__name__
    #   print class_name, "destroyed"