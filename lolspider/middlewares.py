# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
import time

js = """
function scrollToBottom() {

    var Height = document.body.clientHeight,  //文本高度
        screenHeight = window.innerHeight,  //屏幕高度
        INTERVAL = 100,  // 滚动动作之间的间隔时间
        delta = 500,  //每次滚动距离
        curScrollTop = 0;    //当前window.scrollTop 值

    var scroll = function () {
        curScrollTop = document.body.scrollTop;
        window.scrollTo(0,curScrollTop + delta);
    };

    var timer = setInterval(function () {
        var curHeight = curScrollTop + screenHeight;
        if (curHeight >= Height){   //滚动到页面底部时，结束滚动
            clearInterval(timer);
        }
        scroll();
    }, INTERVAL)
}
scrollToBottom()
"""



class JavaScriptMiddleware(object):
    def __init__(self):
        self.driver = webdriver.PhantomJS() #指定使用的浏览器
        self.wait = WebDriverWait(self.driver, 3)

    def process_request(self, request, spider):
        if spider.name =="lol":
            print("PhantomJS is starting...")
            self.driver.get(request.url)
            self.driver.execute_script(js)
            time.sleep(5)
            body = self.driver.page_source
            print("访问"+request.url)
            return HtmlResponse(self.driver.current_url, body=body, encoding='utf-8', request=request)
        else:
            return None