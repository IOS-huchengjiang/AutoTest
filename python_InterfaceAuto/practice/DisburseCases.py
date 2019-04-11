from baseLib.operationManagerAPI import authentication
from baseLib.operationManagerAPI import DisburseManager
from baseLib.operationManagerAPI import feeAudit


def test001():
    modifyDisburseFeeParameter = {'step': '2',
                'oldMethod':'2',
                'merchantId': '46170',
                'type': '5',
                'chargeType': '0',
                'meth': '2',
                'fixFee': '0.02',
                # 'feeRate': '33',
                'minFee': '0.01',
                'maxFee': '6',
                'limitFixRateFund': '500',#额度 （仅在“固定值+费率”的类型下有效！）
                'fixFee1': '',
                'limit1': '',
                'fixFee2': '',
                'limit2': '',
                'fixFee3': '',
                'limit3': '',
                'fixFee4': '',
                'limit4': '',
                'fixFee5': '',
                'limit5': '',
                'limitFund': '45', #单笔限额
                'fld12': '0',#是否手工复核
                'isNeedChildReview': '0',
                'merSingleDayLimit': '',
                'merSingleDayCountLimit': '',
                'merSingleMonthLimit': '',
                'merSingleYearLimit': ''}
    cookie = authentication.login('xjd', 'xjd12345')
    merchantFeeRequestId = str(DisburseManager.mgmodifyDisburseFee(modifyDisburseFeeParameter, cookie)[0][0])
    print(merchantFeeRequestId)
    cookie1 = authentication.login('xjd1', 'xjd12345')
    status = feeAudit.merchantFeeAuditAction_auditConfirm(merchantFeeRequestId, cookie1)
    print(status)

def test002():
    cookie = authentication.login('xjd1', 'xjd12345')
    print(DisburseManager.transferRiskAudit('auto20190312105720051473', cookie))
    print(DisburseManager.transferConfirm('auto20190312105720051473', cookie))

test002()