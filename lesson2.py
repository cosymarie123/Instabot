from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import username, password
import time
import random

def hashtag_search(username, password, hashtag):
    browser = webdriver.Chrome('C:\\Users\\ASUS\\OneDrive\\Desktop\\Instagram_bot\\chromedriver.exe')

    try:
    
        browser.get('https://www.instagram.com/')
        print("OK")
        print("123214124124")
        print("gnasigasignasig")
        time.sleep(random.randrange(3,5))

        username_input = browser.find_element_by_name('username')
        username_input.clear()
        username_input.send_keys(username)

        time.sleep(2)

        password_input = browser.find_element_by_name('password')
        password_input.clear()
        password_input.send_keys(password)

        password_input.send_keys(Keys.ENTER)

        time.sleep(2)

        try:
            browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
            time.sleep(2)

            for i in range(1, 4):
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(random.randrange(3,5))

            hrefs = browser.find_elements_by_tag_name('a')

            posts_urls = [item.get_attribute('href') for item in hrefs if '/p' in item.get_attribute('href')]

            # post_urls = []

            # for item in hrefs:
            #     href = item.get_attribute('href')

            #     if '/p' in href:
            #         post_urls.append(href)
            #         print(href)
            
            for url in posts_urls[0:1]:
                try:
                    browser.get(url)
                    time.sleep(3)
                    like_button = browser.find_elements_by_class_name('wpO6b')[1].click()
                    time.sleep(random.randrange(2,5))
                except Exception as ex:
                    print(ex)   

            browser.close()
            browser.quit()

        except Exception as ex:
            print(ex)
            browser.close()
            browser.quit()

    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()  

hashtag_search(username, password, 'beautiful')        
