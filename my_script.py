from playwright.sync_api import sync_playwright
import os
import time
import requests
if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(
                        # 指定本机用户缓存地址，这是隔离环境的主要点，指定不同的目录存放用户的数据。
                        user_data_dir=USER_DIR_PATH,
                        # 接收下载事件，允许下载需要
                        accept_downloads=True,
                        # 设置 GUI 模式，可以看到浏览器界面
                        headless=False,
                        bypass_csp=True,
                        slow_mo=1000,
                        channel="chrome",
                    )
        page = browser.new_page()

        # 访问Koyeb登录页面
        page.goto("https://freecloud.ltd/login")
        page.wait_for_timeout(10000)
        #print(page.content())

        # 输入邮箱和密码
        #page.fill('input[name="username"]', 'XXXXX')
        #page.fill('input[name="password"]', 'XXXXX')

        # 点击登录按钮
        #page.click('button[type="submit"]')
        

        # 等待可能出现的错误消息或成功登录后的页面
        try:
            # 等待可能的错误消息
            error_message = page.wait_for_selector('.MuiAlert-message', timeout=5000)


        except:
            print(page.content())

        finally:
            browser.close()
