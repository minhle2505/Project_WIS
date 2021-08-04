from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# chrome_options = Options()
# chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--window-size=1920*1080")

driver = webdriver.Chrome(executable_path = "chromedriver.exe")
driver.maximize_window()
driver.get('https://cafef.vn/thi-truong-chung-khoan.chn')
sleep(3)
count_page = 0

while True:
    for i in range(5):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        sleep(2)
    
    links = driver.find_elements_by_xpath('//li[@class="tlitem clearfix ck_success"]/h3/a')
    
    urls = []
    count = 0
    
    for link in links:
        print(link.text)
        url = link.get_attribute('href')
        # print(url)
        urls.append(url)
    
    xemthem = driver.find_element_by_class_name('bt_xemthem')
    xemthem.click()

