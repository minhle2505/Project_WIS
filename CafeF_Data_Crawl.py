from selenium import webdriver
from time import sleep

# chrome_options = Options()
# chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--window-size=1920*1080")

driver = webdriver.Chrome(executable_path = "chromedriver.exe")
driver.get('https://cafef.vn/thi-truong-chung-khoan.chn')

def Crawl_article():
    global count_page
    count_page += 1
    links = driver.find_elements_by_xpath('//*[@id="LoadListNewsCat"]/li[1]')
    urls = []
    count = 0
    #get urls
    for link in links:
        url = link.get_attribute("href")
        urls.append(url)


