# -*- coding:utf-8 -*-
#autor :huchengjiang
import hmac
import hashlib
import random
import time
from baseLib.baseUtils.log import logging

####################设置Key值##############
def md5Signature(param,ekey, rule):
    to_enc = ''
    for i in rule:
        # to_enc = to_enc + param[i]
        to_enc += param[i]
    enc_res = hmac.new(ekey.encode(), to_enc.encode(), hashlib.md5).hexdigest()
    return enc_res

def encodeDictionaryToGBK(dictionary):
    for key in dictionary:
        dictionary[key] = dictionary[key].encode('GBK')
    return dictionary

def requestId():
    # randomNum = []
    randomNum = ''.join(str(i) for i in random.sample(range(0, 9), 6))
    CurrentTime = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    return 'auto' + CurrentTime + randomNum

@logging(level='INFO', desc='执行挂起')
def waiting(sec):
    i = 0
    while  i < sec:
        print('waiting for %s sec' % (sec - i))
        time.sleep(1)
        i += 1

