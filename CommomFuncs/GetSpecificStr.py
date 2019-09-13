#coding:utf-8

#获取特定字符串的方法

class GetSpecificStr:
    def __init__(self):
        pass

    #获取指定字符后的字符串
    def getStrAfter(self,strValue,zifu):  # strValue 为要获取值的字符串，字符为截断位置
        count = 0
        try:
            if type(strValue) != str:
                return "字符类型错误，%s不是字符串"%strValue
            else:
                for i in strValue:
                    if i !=zifu:
                        count+=1
                    else:
                        break
                targetStr = strValue[count:len(strValue)]
                return targetStr
        except Exception as e:
            return "程序出现错误，错误为%s"%e

    #获取指定字符前的字符串
    def getStrBefore(self,strValue,zifu):  # strValue 为要获取值的字符串，字符为截断位置
        count = 0
        try:
            if type(strValue) != str:
                return "字符类型错误，%s不是字符串"%strValue
            else:
                for i in strValue:
                    if i != zifu:
                        count+=1
                    else:
                        break
                targetStr = strValue[0:count]
                return targetStr
        except Exception as e:
            return "程序出现错误，错误为%s"%e


if __name__ == "__main__":
    a = GetSpecificStr()
    print(a.getStrAfter(1,"["))
    print(a.getStrBefore("12345[6789","["))