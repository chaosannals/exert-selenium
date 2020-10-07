import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')   # 无界面化
options.add_argument('--disable-gpu')    # 配合上面的无界面化
options.add_argument('--window-size=1366,768')   # 设置窗口大小, 窗口大小会有影响.
driver = webdriver.Chrome(chrome_options=options)

driver.get('https://baidu.com')
driver.get_screenshot_as_file('baidu.png')
driver.quit()
