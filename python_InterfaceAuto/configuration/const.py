
class _global_configuration(object):
    def __init__(self):
        self.__OracleConnectUri = 'tvpay2/tvpay@172.16.219.99/sumapay'
        self.__OptionManagerHttpUrl = 'http://172.16.9.3:9191'

    @property
    def OracleConnectUri(self):
        return  self.__OracleConnectUri
    @property
    def OptionManagerHttpUrl(self):
        return  self.__OptionManagerHttpUrl