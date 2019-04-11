import requests
from baseLib.baseUtils import OracleQuery
from configuration import const

#费率审核
def merchantFeeAuditAction_auditConfirm(merchantFeeRequestId, cookie):
    merchantFeeAuditActionList = ['/Admin/merchantManage/merchantFeeAuditAction_auditConfirm']
    merchantFeeAuditResponse = requests.get(const._global_configuration().OptionManagerHttpUrl + merchantFeeAuditActionList[0] + '?requestId=' + merchantFeeRequestId,
                                            cookies = cookie)
    responseHtmlStr = merchantFeeAuditResponse.text
    strSQL = 'select status from MERCHANT_FEE_REQUEST where id = %s order by id desc' % merchantFeeRequestId
    return OracleQuery.sqlAll(strSQL)