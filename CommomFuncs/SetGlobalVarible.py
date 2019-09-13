#coding : utf-8
#设置全局变量
import json
from CommomFuncs.GetJsonValue import GetKeyValue
from CommomFuncs.GetSpecificStr import *

class SetGlobalVarible:

    def __init__(self):
        self.gss = GetSpecificStr()


    def setVariable(self,target,variableObject):

        globalVariable = eval(variableObject)  #将传入的字符串转换为dict
        gkv = GetKeyValue(globalVariable, mode="j")  # 实例化获取json的键值
        gkv2 = GetKeyValue(target, mode="j")  # 实例化获取json的键值
        keyList = list(globalVariable.keys())    #获取dict中所有的key
        VariableDict = {}

        for i in keyList:
            value3 = []
            for k in range(0,len(gkv.search_key(i))):  #循环获取变量的值
                value1 = gkv.search_key(i)[k]
                if ("[" or "]") not in value1:
                    a = gkv2.search_key(value1)
                    VariableDict[i] = a[0]
                else:
                    value2 = self.gss.getStrAfter(value1,"[")
                    s = self.gss.getStrBefore(value1,"[")
                    value3.append(s)
                    value4 = "target"+str(value3)+value2
                    m = eval(value4)
                    VariableDict[i] = m
        return VariableDict








if __name__=="__main__":
    result1 = {"state":"true","refresh":"false","topologys":"null","message":"验证码校验正确","data":{"birthday":"818006400000","ssoRefreshToken":"","identityImprove":"Y","validateMessageCode":"true","sex":"F","accessToken":"50017e66da7b03222748d77b97f88eaf214d179fd34b1eb9ed65fc2e63b128dce02c2d22d2da3c39ef871a744f2d5f386909","type":"TEST","accountId":"cocoTest25","uid":"20e1189e-7230-4e75-9ce1-d2d4b652adea","imageCodeVerifyRequired":"false","ssoCookies":"[]","name":"丰静枝","id":"9daa5a1c-21ca-4003-bd8e-18a16f29e5b7","userType":"INNER","refreshToken":"50018d9a2c35647c069545a903a44d541304096623c739df1e066301e1bf8004f8b94390b00aa1a2b3c03757430420e4d0ea"}}
    a = SetGlobalVarible()
    s = a.setVariable(result1,'''{'token':'data["accessToken"]','uid':'data["uid"]'}''',)
    print(s)
