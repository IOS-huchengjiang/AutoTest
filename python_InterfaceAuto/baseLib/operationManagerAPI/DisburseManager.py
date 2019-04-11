import requests
from lxml import etree
from baseLib.baseUtils import OracleQuery
from configuration import const
from baseLib.baseUtils.log import logging


#代发费率修改
@logging(level='INFO', desc='修改付款费率')
def mgmodifyDisburseFee(inputFormParam, cookie):
    mgmodifyActionList = ['/Admin/withdrawManage/merchantTransferConfigManageAction_mgtoUpdateBatchpay',
                          '/Admin/withdrawManage/merchantTransferConfigManageAction_mgmodifyBatchpay']
    getTokenParam = '?merchantId=' + inputFormParam.get('merchantId') + '&type=' + inputFormParam.get('type') + '&meth=' + inputFormParam.get('meth')
    getTokenResponseHtmlStr = requests.get(
        const._global_configuration().OptionManagerHttpUrl + mgmodifyActionList[0] + getTokenParam,
        cookies=cookie)
    selector = etree.HTML(getTokenResponseHtmlStr.text)
    try:
        strToken = (selector.xpath('//input[@name=\"token\"]/@value'))[0].strip()
    except IndexError:
        strToken = 'none'
    hideFormParam = {'struts.token.name': 'token',
                 'token': strToken}
    allFormParam = hideFormParam.copy()
    allFormParam.update(inputFormParam)
    responseByPostForm = requests.post(const._global_configuration().OptionManagerHttpUrl + mgmodifyActionList[1],
                                       cookies=cookie,
                                       data = allFormParam)
    responseHtmlStr = responseByPostForm.text

    # strSQL = 'select id from MERCHANT_FEE_REQUEST where merchant_id = %s and type = %s and status = %s order by id desc'%(inputFormParam.get('merchantId'),inputFormParam.get('type'), '0')
    # return OracleQuery.sqlAll(strSQL)

#风控通过
@logging(level='INFO', desc='风控通过')
def transferRiskAudit(merchantTransferRequestId, cookie):
    sqlId = 'select id from merchant_transfer_request where request_id = \'%s\'' %merchantTransferRequestId
    indexId = OracleQuery.sqlOne(sqlId)[0]
    transferRiskAuditActionList = ['/Admin/withdrawManage/merchantWithdrawManageAction_query',
                          '/Admin/withdrawManage/merchantWithdrawManageAction_mgconfirm?requestId=%s&fld1=0'%(indexId)]
    getTokenParam = {'requestDateStart': '2999/03/12'}
    getTokenResponseHtmlStr = requests.post(
        const._global_configuration().OptionManagerHttpUrl + transferRiskAuditActionList[0],
        cookies=cookie, data = getTokenParam)
    selector = etree.HTML(getTokenResponseHtmlStr.text)
    try:
        strToken = (selector.xpath('//input[@name=\"token\"]/@value'))[0].strip()
    except IndexError:
        strToken = 'none'
    hideFormParam = {'struts.token.name': 'token',
                 'token': strToken}
    allFormParam = hideFormParam.copy()
    responseByPostForm = requests.post(const._global_configuration().OptionManagerHttpUrl + transferRiskAuditActionList[1],
                                       cookies=cookie,
                                       data = allFormParam)
    responseHtmlStr = responseByPostForm.text

#财务通过
@logging(level='INFO', desc = '财务通过')
def transferConfirm(merchantTransferRequestId, cookie):
    sqlId = 'select id from merchant_transfer_request where request_id = \'%s\'' % merchantTransferRequestId.decode()
    indexId = OracleQuery.sqlOne(sqlId)[0]
    transferRiskAuditActionList = ['/Admin/withdrawManage/merchantWithdrawManageAction_query',
                                   '/Admin/withdrawManage/merchantWithdrawManageAction_mgfinanceConfirm?requestIds=%s|0' % (
                                       indexId)]
    getTokenParam = {'requestDateStart': '2999/03/12'}
    getTokenResponseHtmlStr = requests.post(
        const._global_configuration().OptionManagerHttpUrl + transferRiskAuditActionList[0],
        cookies=cookie, data=getTokenParam)
    selector = etree.HTML(getTokenResponseHtmlStr.text)
    try:
        strToken = (selector.xpath('//input[@name=\"token\"]/@value'))[0].strip()
    except IndexError:
        strToken = 'none'
    hideFormParam = {'struts.token.name': 'token',
                     'token': strToken}
    allFormParam = hideFormParam.copy()
    # allFormParam.update(inputFormParam)
    responseByPostForm = requests.post(
        const._global_configuration().OptionManagerHttpUrl + transferRiskAuditActionList[1],
        cookies=cookie,
        data=allFormParam)
    responseHtmlStr = responseByPostForm.text


