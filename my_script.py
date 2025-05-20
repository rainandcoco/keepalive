from DrissionPage import Chromium
from DrissionPage import ChromiumOptions


# 创建浏览器启动配置对象
options = ChromiumOptions()
# 配置浏览器启动选项
options.set_browser_path(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')  # 设置浏览器路径
options.ignore_certificate_errors() # 忽略证书错误
options.no_imgs()  # 禁用图片
options.headless(False)  # 无头模式
options.set_local_port(9696)  # 设置浏览器debug端口
# 更多配置请参考 http://drissionpage.cn/browser_control/browser_options


# 连接浏览器并获取浏览器对象
browser = Chromium(options) 

# 获取标签页对象并打开网址
tab = browser.new_tab('https://www.baidu.com')



input('Press any key to quit')  
