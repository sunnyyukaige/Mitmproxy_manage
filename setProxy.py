import subprocess
import unittest


class SetProxy(unittest.TestCase):
    networkTypes = ['Ethernet', 'Thunderbolt Ethernet', 'Wi-Fi']

    def enable_global_proxy(self, networkType= networkTypes[0], ip='127.0.0.1', port='8080'):
        scp = 'networksetup -setsecurewebproxy {networkType} {ip} {port} && networksetup -setproxybypassdomains {networkType} 127.0.0.1 localhost mockserver.ff-svc.cn'.format(networkType=networkType, ip=ip, port=port)
        try:
            return subprocess.Popen(scp, shell=True)
        except Exception as e:
            raise e

    def disable_global_proxy(self, networkType= networkTypes[0]):
        scp= 'networksetup -setsecurewebproxystate {networkType} off'.format(networkType=networkType)
        try:
            return subprocess.Popen(scp,shell=True)
        except Exception as e:
            raise e

    def test_function(self):
        self.enable_global_proxy(self.networkTypes[2])
        self.disable_global_proxy(self.networkTypes[2])