# -*- coding:utf-8 -*-
#autor :huchengjiang
import requests
import time
import random
from baseLib.baseUtils import commonUtils
import unittest

class transfer(unittest.TestCase):

    def setUp(self):
        self.headers={
            'Connection': 'keep-alive',
            'Content-Length': '543',
            'Cache-Control': 'max-age=0',
            'Origin': 'http://172.16.3.2:9292',
            'Upgrade-Insecure-Requests': '1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Referer': 'http://172.16.3.2:9292/testpayMobile/sbTransferSignatureServlet',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

    def test001(self):
        print("开始进行单笔代发测试： ")
        url = 'http://172.16.3.2:9292/main/singleTransfer_toTransfer'
        id = []
        id = ''.join(str(i) for i in random.sample(range(0, 9), 2))  # sample(seq, n) 从序列seq中选择n个随机且独立的元素；
        CurrentTime = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        print(type(CurrentTime))
        requestid = CurrentTime + id

        payload = {'requestId': '',
                   'merchantCode': 'CSSH',
                   'transferType': '1',
                   'transToMerCode': '',
                   'transToMerName': '',
                   'unionBankNum': '',
                   'openBankName': '',
                   'openBankProvince': '',
                   'openBankCity': '',
                   'sum': '0.03',
                   'accountType': '1',
                   'accountName': '武孟梦',
                   'bankCode': 'icbc',
                   'bankAccount': '6212260200036759963',
                   'reason': '1555',
                   'noticeUrl': 'http://172.16.3.1/testpayMobile/p2pNoticeGBK',
                   'refundNoticeUrl': 'http://172.16.3.1/testpayMobile/p2pNoticeGBK',
                   'transferPayType': '1',
                   'signature': ''
                   }
        payload['requestId'] = requestid
        # 初始化字符串并进行加密拼接
        to_enc = ''
        ekey = 'CSSH_KEY'
        for i in payload:
            to_enc = to_enc + payload[i]
        # print(to_enc)
        payload['signature'] = commonUtils.hashstring(to_enc, ekey)

        '''将中文进行GBK转化'''
        accountName = '武孟梦'
        strGBK = accountName.encode('GBK')

        '''转化完的中文回传到字典中'''
        payload['accountName'] = strGBK

        headers = self.headers
        s = requests.post(url=url, data=payload, headers=headers)
        print(s.text)
        print("status:", s.status_code)
        print("****************************************************")
        print("开始进行返回结果验证签名: ")
        '''返回结果进行验签'''
        ResultDict = s.json()
        synchronizationStr = ResultDict['requestId'] + ResultDict['result'] + ResultDict['sum']
        signature11 = commonUtils.hashstring(synchronizationStr, ekey)
        try:
            if (ResultDict['result'] == '00000' and signature11 == ResultDict['signature']):
                print("                    恭喜你，同步返回验签成功")
            else:
                print("                    result错误码:", ResultDict['result'])
        except BaseException as msg:
            print(msg)
        finally:
            print("                    代发处理完毕")
        print("****************************************************")
    def test002(self):
        print("开始进行批量代发测试： ")
        url = 'http://172.16.3.2:9292/main/BatchTransfer_notifyCheck'
        id = []
        id = ''.join(str(i) for i in random.sample(range(0, 9), 2))  # sample(seq, n) 从序列seq中选择n个随机且独立的元素；
        CurrentTime = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        print(type(CurrentTime))
        requestid = CurrentTime + id

        payload = {'merchantCode': 'CSSH',
                   'requestId': '',
                   'batchTransferNo': '201902270002',
                   'payType': '2',
                   'inAccountType': '1',
                   'transferPayType': '',
                   'signature': ''
                   }
        payload['requestId'] = requestid
        # 初始化字符串并进行加密拼接
        to_enc = ''
        ekey = 'CSSH_KEY'
        for i in payload:
            to_enc = to_enc + payload[i]
        # print(to_enc)
        payload['signature'] = commonUtils.hashstring(to_enc, ekey)

        headers = self.headers
        s = requests.post(url=url, data=payload, headers=headers)
        print(s.text)
        print("status:", s.status_code)
        print("****************************************************")
        # print("开始进行返回结果验证签名: ")
        # '''返回结果进行验签'''
        # ResultDict = s.json()
        # synchronizationStr = ResultDict['requestId'] + ResultDict['result'] + ResultDict['sum']
        # signature11 = MD5Signature.hashstring(synchronizationStr, ekey)
        # try:
        #     if (ResultDict['result'] == '00000' and signature11 == ResultDict['signature']):
        #         print("                    恭喜你，同步返回验签成功")
        #     else:
        #         print("                    result错误码:", ResultDict['result'])
        # except BaseException as msg:
        #     print(msg)
        # finally:
        #     print("                    代发处理完毕")
        # print("****************************************************")


    def tearDown(self):
        time.sleep(3)


if __name__=='__main__':
    unittest.main()










# def singletransfer():










