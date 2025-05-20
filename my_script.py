
# 连接浏览器并获取浏览器对象
browser = Chromium()  

# 获取标签页对象并打开网址

tab1 = browser.new_tab('https://www.baidu.com')
tab2 = browser.new_tab('https://www.bing.com')
tab3 = browser.latest_tab

print(tab1.title)
print(tab2.title)
print(tab3.title)
print(browser.latest_tab.title)

browser.latest_tab.close()  # 关闭最新的标签页


# 标签页没有Selenium所谓的焦点的概念，多个标签页可以并行操作，所以可以多线程同时打开多个标签页


from concurrent.futures import ThreadPoolExecutor


def open_url(browser,url): 
    
    browser.new_tab(url)

chinese_websites = [
    "https://www.taobao.com",     # 淘宝
    "https://www.tmall.com",      # 天猫
    "https://www.jd.com",          # 京东
]    

# 使用线程池
with ThreadPoolExecutor(max_workers=3) as executor:
    for url in chinese_websites:
        executor.submit(open_url, browser,url)



input('请按任意键继续')
