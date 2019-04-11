import requests
from baseLib.baseUtils import invokeJar
import re
from configuration import const
from baseLib.baseUtils.log import logging

#运营管理登录
@logging(level='INFO', desc='运营管理登录')
def login(strUserName, strPassword):
    loginActionList = ['/Admin/queryUserNameAction_srandNum?time=1540957646874',
                       '/Admin/j_spring_security_check']
    getSrandNumResponse = requests.get(const._global_configuration().OptionManagerHttpUrl + loginActionList[0])
    responseCookies = getSrandNumResponse.cookies
    strSandNum = re.findall(r"%7B%27mcryptKey%27%3A%27(.+?)%27%7D",getSrandNumResponse.text)
    strEncodePassword = invokeJar.getEncodePassword(strSandNum[0], strPassword)

    securityCheckFormPara = {'phone':'',
                             'randomValidateId':'',
                             'sendFlag':'',
                             'userNameOld': strUserName,
                             'password': strEncodePassword,
                             'passwordtype': '1',
                             'j_username': strUserName,
                             'validate':'',
                             'message':''}
    responseByPostForm = requests.post(const._global_configuration().OptionManagerHttpUrl + loginActionList[1],
                                       cookies = responseCookies,
                                       data = securityCheckFormPara)

    responseCookies.update(responseByPostForm.cookies)
    responseCookies.set('tvpay_login_name', strUserName)
    return responseCookies