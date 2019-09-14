import xdrlib
import json
import time
import requests
from ApiTest.ApiFuncs.nuc_funcs import CocoApi
from ApiTest.CommomFuncs.GetJsonValue import GetKeyValue

class Coco:
    def group_dismissGroup(self,token,uid,groupId):
        req_header = {'Content-Type': 'application/json;charset=UTF-8'}
        apiBody = {  "deviceType":"ios",
                            "appKey":"coco",
                            "token":token,
                            "userId":uid,
                            "groupId":groupId
                        }
        body = json.dumps(apiBody)
        res = requests.post("https://iocp-di2.sit.cmrh.com/iocp-msg-api/group-dismissGroup",data=body,headers = req_header)
        print(res.json())


if __name__=="__main__":
    url = "https://iocp-di2.sit.cmrh.com/iocp-msg-api/user-getUserInfoListByUid"
    header = {'Content-Type': 'application/json;charset=UTF-8'}
    apiBody = {"deviceType":"ios", "userId":"20e1189e-7230-4e75-9ce1-d2d4b652adea", "appKey":"coco", "token":"50017e66da7b03222748d77b97f88eaf214d9d44de904837c3afb497c9574ee646d406a677c7a35d42c31b3bf2cca55ff3bb", "counterPartId": "20e1189e-7230-4e75-9ce1-d2d4b652adea"}
    c = CocoApi()
    result1 = c.commonRequest("post",url,header,apiBody)
    b = GetKeyValue(result1.json(),mode="j")

    groupList = b.search_key("groups")[0]

    a = Coco()
    for i in groupList:
        j = int(i)
        a.group_dismissGroup('50017e66da7b03222748d77b97f88eaf214d9d44de904837c3afb497c9574ee646d406a677c7a35d42c31b3bf2cca55ff3bb',"20e1189e-7230-4e75-9ce1-d2d4b652adea",j)

