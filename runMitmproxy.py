from setProxy import SetProxy
import subprocess
from mitmproxy import master
from mitmproxy import options
import time


class setMitmproxy:
    @staticmethod
    def start_mitmproxy():
        setProxy = SetProxy()
        setProxy.enable_global_proxy(SetProxy.networkTypes[2])
        scp = 'mitmdump -s hostMapping.py'
        try:
            return subprocess.Popen(scp, shell=True)
        except Exception as e:
            raise e

    @staticmethod
    def stop_mitmproxy():
        scp = "kill -9 $(ps aux| grep -i mitmdump |awk '{print $2}')"
        try:
            return subprocess.Popen(scp, shell=True)
        except Exception as e:
            raise e
        finally:
            SetProxy().disable_global_proxy(SetProxy.networkTypes[2])


if __name__ == '__main__':
    setMitmproxy.start_mitmproxy()
    time.sleep(5)
    setMitmproxy.stop_mitmproxy()
