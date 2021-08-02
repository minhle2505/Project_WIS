from selenium import webdriver
from time import sleep

# chrome_options = Options()
# chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--window-size=1920*1080")

driver = webdriver.Chrome(executable_path = "D:\chromedriver_win32\chromedriver.exe")
driver.get('https://cafef.vn/thi-truong-chung-khoan.chn')
sleep(3)
count_page = 0

# SCROLL_PAUSE_TIME = 0.5

# # Get scroll height
# last_height = driver.execute_script("return document.body.scrollHeight")

# while True:
#     # Scroll down to bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#     # Wait to load page
#     sleep(SCROLL_PAUSE_TIME)

#     # Calculate new scroll height and compare with last scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height

def Crawl_article():
    global count_page
    count_page += 1
    # links = driver.find_element_by_xpath('//*[@id="LoadListNewsCat"]/li[1]/h3/a')
    links = driver.find_elements_by_tag_name('a')
    urls = []
    count = 0
    #get urls
    for link in links:
        url = link.get_attribute("href")
        urls.append(url)
        print(urls, "This is the urls we are looking for")
Crawl_article()
