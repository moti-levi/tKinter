import json
#handle Test_definition.json 

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
        retList=[] 
        f = open(str(_jsonFileName))        
        # returns JSON object as
        # a dictionary
        data = json.load(f)
        #definitionData=data.get(definition)
        for scriptNum in scriptNumber:
            scriptFilesTime=data.get(str(scriptNum)).get('Duration')            
            retList.append(int(scriptFilesTime))
        # Closing file
        f.close()
        return retList
        
    def ReadDefinisionFileNameAndNumber(_jsonFileName):
        # Opening JSON file
        # f = open(str(_jsonFileName))
         # returns JSON object as
        # a dictionary
        RetDict={}
        with open(_jsonFileName, encoding="utf-8") as f:
            data = json.load(f)
            # print(data)
       
        for i in data:
            scriptFile=data[i]['Test Name']
            scriptNum=data[i]['Test Number']
            RetDict[scriptFile]=scriptNum        
        # Closing file
        f.close()
        return RetDict

    def UpdateJsonDefinitionFile(_jsonFileName,_jsonSection,_data,_TestType):
        # Opening JSON file
        
        with open(_jsonFileName, 'r') as f:
            json_data = json.load(f)            
            for i in json_data:
                if i==_TestType:
                    json_data[i][_jsonSection]=_data                
        
        with open(_jsonFileName, 'w') as f:
            f.write(json.dumps(json_data))        
            # Closing file
            f.close()
    #update last succeess test time at Test_definition.json 
    def UpdateJsonDefinitionSuccessTime(_jsonFileName,CurrentTestTime,TestName):
        # Opening JSON file
        
        with open(_jsonFileName, 'r') as f:
            json_data = json.load(f)            
            for i in json_data:
                if TestName in json_data[i]['PC scripts']:
                    json_data[i]['Duration']=CurrentTestTime                
        
        with open(_jsonFileName, 'w') as f:
            # f.write(json.dumps(json_data))  
            json.dump(json_data, f, ensure_ascii=True, indent=4, sort_keys=True)      
            # Closing file
            f.close()

    
    def __del__(self):
      class_name = self.__class__.__name__
    #   print class_name, "destroyed"