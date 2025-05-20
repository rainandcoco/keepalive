from DrissionPage import Chromium

# 连接浏览器并获取浏览器对象
browser = Chromium()  

# 获取标签页对象并打开网址
tab = browser.new_tab('https://www.baidu.com')



input('Press any key to quit')
