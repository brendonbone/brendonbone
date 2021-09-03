from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time

proxy_ip_port = '128.199.250.178:3128'

proxy = Proxy() 
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = proxy_ip_port
proxy.ssl_proxy = proxy_ip_port

capabilities = webdriver.DesiredCapabilities.CHROME
proxy.add_to_capabilities(capabilities)

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get('https://www.wisortutoring.com/request-a-quote', desired_capabilities=capabilities)

time.sleep(8)

driver.quit

