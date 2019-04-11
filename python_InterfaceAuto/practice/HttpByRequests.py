import requests
import codecs
from lxml import etree

# r = requests.get('http://www.baidu.com')
# print(r.text)

disburseType = '普通付款至个人银行'
formPara = {'merchantId1':'104'}
action = 'http://172.16.9.3:9191/Admin/withdrawManage/merchantTransferConfigManageAction_queryBatchpay'

def queryDisburseFee():
    responseByPostForm = requests.post(action, data = formPara)
    responseHtmlStr = responseByPostForm.text
    # print(responseHtmlStr)
    selector = etree.HTML(responseHtmlStr)
    # print(etree.tostring(selector))
    # str = (selector.xpath('/html/body/form/table/tr[3]/td/table/tr[2]/td[5]/text()'))[0].strip()
    str = (selector.xpath('//table[@id=\'ProviderListTbl\']/tr/td[contains(text(),"' + disburseType + '")]/../td[9]/text()'))[0].strip()
    str1 = (selector.xpath('//table[@id=\'ProviderListTbl\']/tr/td[contains(text(),"' + disburseType + '")]/../td[5]/text()'))[0].strip()
    print(str)
    return (str, str1)

# def getMerchantId(strMerchantName, strMerchantCode, token):
#     action = 'http://' + ip + '/Admin/withdrawManage/merchantTransferConfigManageAction_initBatchpay'
#     responseByGet = requests.get(action, cookies=token)
#     responseHtmlStr = responseByGet.text
#     print(responseHtmlStr)
#     selector = etree.HTML(responseHtmlStr)
#     try:
#         strMerchantId = (selector.xpath(
#             '//select[@id=\"merchantIdSelect\"]/option[contains(text(),"' + strMerchantName + '-' + strMerchantCode + '")]/@value'))[
#             0].strip()
#     except IndexError:
#         strMerchantId = 'none'
#     return strMerchantId

def queryDisburseFee(strMerchantId, strDisburseType, cookie):
    action = 'http://' + ip + '/Admin/withdrawManage/merchantTransferConfigManageAction_queryBatchpay'
    # action = 'http://172.16.9.3:9191/Admin/withdrawManage/merchantTransferConfigManageAction_queryBatchpay'
    formPara = {'merchantId1': strMerchantId}
    responseByPostForm = requests.post(action, cookies=cookie, data = formPara)
    responseHtmlStr = responseByPostForm.text
    # print(responseHtmlStr)
    selector = etree.HTML(responseHtmlStr)
    # print(etree.tostring(selector))
    # str = (selector.xpath('/html/body/form/table/tr[3]/td/table/tr[2]/td[5]/text()'))[0].strip()
    try:
        strMerchantName = (selector.xpath(
            '//table[@id=\'ProviderListTbl\']/tr/td[contains(text(),"' + strDisburseType + '")]/../td[4]/text()'))[
            0].strip()
    except IndexError:
        strMerchantName = 'none'
    try:
        strFeeType = (selector.xpath(
            '//table[@id=\'ProviderListTbl\']/tr/td[contains(text(),"' + strDisburseType + '")]/../td[6]/text()'))[
            0].strip()
    except IndexError:
        strFeeType = 'none'
    try:
        strRateType = (selector.xpath(
            '//table[@id=\'ProviderListTbl\']/tr/td[contains(text(),"' + strDisburseType + '")]/../td[7]/text()'))[
            0].strip()
    except IndexError:
        strRateType = 'none'
    try:
        strFix = (selector.xpath(
            '//table[@id=\'ProviderListTbl\']/tr/td[contains(text(),"' + strDisburseType + '")]/../td[8]/text()'))[
            0].strip()
    except IndexError:
        strFix = 'none'
    try:
        strRate = (selector.xpath(
            '//table[@id=\'ProviderListTbl\']/tr/td[contains(text(),"' + strDisburseType + '")]/../td[9]/text()'))[
            0].strip()
    except IndexError:
        strRate = 'none'

    try:
        strManualCheck = (selector.xpath(
            '//table[@id=\'ProviderListTbl\']/tr/td[contains(text(),"' + strDisburseType + '")]/../td[12]/text()'))[
            0].strip()
    except IndexError:
        strManualCheck = 'none'

    return (strMerchantName, strFeeType, strRateType, strFix, strRate, strManualCheck)

# print(queryDisburseFee())


