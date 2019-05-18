from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import requests
from bs4 import BeautifulSoup
URL = 'https://www.naver.com/'
html = requests.get(URL).text
soup = BeautifulSoup(html, 'html.parser')
tweets = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k')
count = 1
for tweet in tweets:
    print('    ' + str(count) + '. ' +  tweet.text)
    print('\n')
    count += 1

# driver = webdriver.Chrome('./chromedriver')

# driver.get(URL)
# driver.get(f'https://search.naver.com/search.naver?where=realtime&sm=tab_nmr&query={word}')

# ah_ico_open = driver.find_element_by_class_name('PM_CL_realtimeKeyword_rolling')
# ah_ico_open = driver.find_elements_by_css_selector('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div')
# one_to_ten = driver.find_element_by_class_name('ah_ico_open')
# for _ in range(3):
#     if more_button:
#         more_button.click()
#         sleep(2)
#     else:
#         break

# ActionChains(driver).move_to_element(ah_ico_open).perform()
# sleep(5)
# tweets = driver.find_elements_by_css_selector('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li:nth-child(1) > a > span.ah_k')
# tweets = driver.find_elements_by_css_selector('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li >a >span.ah_k')


# print(texts)
# for text in texts:
#     print(text + '\n')

# driver.quit()