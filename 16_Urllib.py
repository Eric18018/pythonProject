import urllib3
import urllib
from urllib import request

if __name__ == '__main__':

    # 以下为Python3.7下urllib、urllib2、urllib3的属性、方法列表
    # print(dir(urllib))
    # print(dir(urllib.request))
    # print(dir(urllib3))

    # 通过request访问数据
    # resp = request.urlopen("http://image.baidu.com/")
    # print(resp.read().decode())

    http = urllib3.PoolManager()
    resp_dat = http.request('GET', "http://image.baidu.com/")
    print(resp_dat.data.decode())
