from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from capmonster_python import NoCaptchaTaskProxyless
options = Options()
driver = webdriver.Chrome(options=options, executable_path="C:\Program Files (x86)\chromedriver.exe")
driver.get("https://www.google.com/recaptcha/api2/demo")

website_key = "wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ" #Checking if different website keys work
website_url = driver.current_url

captcha = NoCaptchaTaskProxyless(client_key="da950b4af117f859d3c61d347e6472c0")
taskId = captcha.createTask(website_url, website_key)
print("# Task created successfully, waiting for the response.")
response = captcha.joinTaskResult(taskId)
print("# Response received.")
driver.execute_script(f"document.getElementsByClassName('g-recaptcha-response')[0].innerHTML = '{response}';")
print("# Response injected to secret input.")
