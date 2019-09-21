import xdrlib
import json
import time
import requests
from CommomFuncs.GetJsonValue import GetKeyValue
from CommomFuncs.SetGlobalVarible import *

class CocoApi:
    def __init__(self):
        self.sgv = SetGlobalVarible()

#定义通用接口方案
    def commonRequest(self,reqType,apiUrl,headers,apiBody):

        if str(reqType).upper() == "POST":
            if type(apiBody) != dict:
                body = eval(apiBody)
                body = json.dumps(body)
            else:
                body = json.dumps(apiBody)
            global res
            res = requests.post(apiUrl,data=body,headers=headers)
            print(res.text)
            return res



        elif reqType.Upper() == "GET":
            pass

        else:
            pass



    #校验接口的返回值
    def request_v(self,expInfo,expStaus):
        try:
            gkv = GetKeyValue(res.json(), mode="j")
            expInfo = eval(expInfo)
            expKeyList = list(expInfo.keys())

            if expStaus.upper() == "TRUE":
                for i in expKeyList:
                    if expInfo[i] == gkv.search_key(i)[0]:
                        continue
                    else:
                        print("FAIL,测试失败，期望的结果为%s:%s，实际结果为%s:%s"%(i,expInfo[i],i,gkv.search_key(i)))
                        return "FAIL,测试失败，期望的结果为%s:%s，实际结果为%s:%s"%(i,expInfo[i],i,gkv.search_key(i))
                print("PASS,用例测试成功")
                return "PASS,用例测试成功"
            else:
                pass


        except Exception as e:
            print("%s"%e)
        pass

if __name__ == "__main__":

    header3 = {'Content-Type': 'application/json;charset=UTF-8','cookie':""}
    a = CocoApi()
    result = a.commonRequest("post","https://iocp-di1.sit.cmrh.com/LoginApp/v1/loginWithTwoFactorsAuth",{'Content-Type': 'application/json;charset=UTF-8'},{"accountId":"cocoTest25","password":"Pass@word1","verifyCode":"","options":{"moduleCode":"IOCP_COCO","authType":"passwdMobile"}})
    bianliang = a.sgv.setVariable(result.json(),'''{'mid':'data["messageId"]','mcd':'data["messageCode"]'}''',)
    result1 = a.commonRequest("post","https://iocp-di1.sit.cmrh.com/LoginApp/v1/validateMessageCode",{'Content-Type': 'application/json;charset=UTF-8'},{"messageCode":bianliang["mcd"],"messageId":bianliang["mid"]})
    # token = result1.json()["data"]["accessToken"]
    # uid = result1.json()["data"]["uid"]
    # header3["cookie"] = "_a="+token
    # a.commonRequest("post","https://iocp-di1.sit.cmrh.com/iocp-msg-api/user-newBindTokens",header3,{"deviceType":"ios","userId": uid,"deviceToken":1234567890123,"appKey":"coco","token": token})
    # #正确名称能够添加成功
    # #a.commonRequest("post",'https://iocp-di1.sit.cmrh.com/iocp-msg-api/application/addApplication',header3,{"appName":"测试添加1","appDesc":"11111"})
    #
    # a.request_v('{"_id":"20e1189e-7230-4e75-9ce1-d2d4b652adea","uid":"20e1189e-7230-4e75-9ce1-d2d4b652adea"}',"true")

