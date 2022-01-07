import codecs
import re
from urllib import request, parse
import datetime


class html_cont_analy(object):

    def download(self, url):
        html_cont1 = request.urlopen(url).read().decode('utf-8')
        com_cont = re.compile(
            r'<div id="mainbody">.*?zwconttbn.*?<a.*?<font>(.*?)</font>.*?<div.*?class="zwcontentmain.*?">.*?"zwconttbt">(.*?)</div>.*?social clearfix',
            re.DOTALL)

        try:
            # cont=com_cont.search(html_cont1).group()
            conts = re.findall(com_cont, html_cont1)
            for item in conts:
                if (item[0] != u"财经评论") and (item[0] != u"东方财富网"):
                    return u"散户ID-" + item[0] + item[1] + "\n"
                else:
                    return u"官方-" + item[0] + item[1] + "\n"
        except Exception as e:
            print("NO HTML")
            return "NO HTML"

    def find_time(self, url):
        html_cont2 = request.urlopen(url).read().decode('utf-8')
        pub_elems = re.search('<div class="zwfbtime">.*?</div>', html_cont2).group()
        try:
            pub_time = re.search('\d\d\d\d-\d\d-\d\d', pub_elems).group()
            dt = datetime.strptime(pub_time, "%Y-%m-%d")  # 字符串转时间格式
            return datetime.date(dt)
        except Exception as e:
            print("NO HTML")
            return datetime.datetime.now().date() + datetime.timedelta(days=1)


class crawer_task(object):
    def __init__(self):
        self.target_page = target_url_manager('http://guba.eastmoney.com/list,usqd,')
        self.downloader = html_cont_analy()
        self.outputer = output_txt()

    def apply_run(self, sumpage):
        file_txt = self.outputer.open_txt()
        error_time = 0
        true_time = 0
        time_start = datetime.datetime.now().date()  # 获取日期信息
        self.target_page.add_pages_urls(sumpage)  # 获取论坛网页URL地址队列

        while self.target_page.has_page_url():
            new_urls = self.target_page.get_new_url()  # 获取每个帖子的URL地址队列
            for url in new_urls:
                if time_start <= (self.downloader.find_time(url) + datetime.timedelta(days=30)):
                    self.outputer.out_txt(file_txt, self.downloader.download(url))
                    true_time = true_time + 1
                else:
                    error_time = error_time + 1
                    if error_time >= 10: break
        print('%s has a sum of %d comments' % (time_start, true_time))
        self.outputer.close_txt(file_txt)
        return


class target_url_manager(object):

    def __init__(self, st_url):

        self.target_urls = list()  # 创建队列
        self.store_urls = list()
        self.general_url = st_url

    def add_page_urls(self, i):

        item_urls = list()
        html_cont = request.urlopen(self.general_url + 'f_%d.html' % i).read().decode('utf-8')
        pattern = re.compile('/news\S+html', re.S)
        news_comment_urls = re.findall(pattern, html_cont)  # 非空白字符N次
        for comment_url in news_comment_urls:
            whole_url = parse.urljoin(self.general_url, comment_url)
            item_urls.append(whole_url)
        return item_urls

    def add_pages_urls(self, n):  # 网页数量
        for i in range(1, n + 1):
            self.target_urls.append(self.add_page_urls(i))  # 增加列表成员
        self.target_urls.reverse()
        return

    def has_page_url(self):
        return len(self.target_urls) != 0

    def get_new_url(self):
        next_url = self.target_urls.pop()  # 去除列表成员
        self.store_urls.append(next_url)
        print(next_url)
        return next_url


class output_txt(object):

    def open_txt(self):
        name = "stock_cont.txt"
        try:
            f = codecs.open(name, 'a+', 'utf-8')
        except Exception as e:
            print("NO TXT")
        return f

    def out_txt(self, f_handle, conts):
        try:
            print("cont", conts)
            f_handle.write(conts)
        except Exception as e:
            print("NO FILE")

    def close_txt(self, f_handle):
        f_handle.close()


if __name__ == '__main__':
    sumpage = 3
    obj_crawer = crawer_task()
    obj_crawer.apply_run(sumpage)
