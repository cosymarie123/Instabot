from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from auth_data import username, password
import time
import random
from selenium.common.exceptions import NoSuchElementException

class InstagramBot():

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    def close_browser(self):
        self.browser.close()
        self.browser.quit()

    def login(self):

        browser = self.browser
        browser.get('https://www.instagram.com/')
        time.sleep(random.randrange(3,5))

        username_input = browser.find_element_by_name('username')
        username_input.clear()
        username_input.send_keys(username)

        time.sleep(2)

        password_input = browser.find_element_by_name('password')
        password_input.clear()
        password_input.send_keys(password)
        time.sleep(2)
        password_input.send_keys(Keys.ENTER)

        time.sleep(5)

    def like_photo_by_hashtag(self, hashtag):
        browser = self.browser

        browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
        time.sleep(2)

        for i in range(1, 4):
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(random.randrange(3,5))


        posts_urls = [item.get_attribute('href') for item in hrefs if '/pqa' in item.get_attribute('href')]
            
        for url in posts_urls:
            try:
                browser.get(url)
                time.sleep(3)
                like_button = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div/article/div/div[2]/div/div[2]/section[1]/span[1]/button').click()
                time.sleep(random.randrange(2,5))
            except Exception as ex:
                print(ex)   
                self.close_browser()
#Tìm phần tử trong 1 trang
    def xpath_exists(self, url):
        browser = self.browser
        try:
            browser.find_element_by_xpath(url)
            exist = True   
        except NoSuchElementException:
            exist = False
        return exist
#Giá trị giảm dần
    def put_exactly_like(self, userpost):

        browser = self.browser
        browser.get(userpost)
        time.sleep(4)

        wrong_userpage = '/html/body/div[1]/section/main/div/div/h2'      
        if self.xpath_exists(wrong_userpage):
            print("Url Error")
            self.close_browser()
        else:
            print("Post and like confession")
            time.sleep(2)              
            like_button = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button').click()
            time.sleep(2) 

            print(f'Post {userpost} Successful')
            self.close_browser()
#Vào profile và like tất cả bài đăng
    def put_many_likes(self, userpage):
        browser = self.browser
        browser.get(userpage)
        time.sleep(4)

        wrong_userpage = '/html/body/div[1]/section/main/div/div/h2'      
        if self.xpath_exists(wrong_userpage):
            print("Url Error")
            self.close_browser()
        else:
            print("Post and like confession")
            time.sleep(2) 

            post_count = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[1]/div/span').text
            loops_count = int(post_count / 12)
            print(loops_count)

            post_urls = []

            for i in range(0, loops_count):
                hrefs = browser.find_elements_by_tag_name('a')

                hrefs = [item.get_attribute('href') for item in hrefs if '/p' in item.get_attribute('href')]

                for href in hrefs:
                    post_urls.append(href)

                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")   
                time.sleep(random.randrange(2, 4))
                print(f"Loading #{i}")

            file_name = userpage.split('/')[-2]    

            with open (f'C:\\Users\\ASUS\\OneDrive\\Desktop\\Instagram_bot\\{file_name}.txt', 'a') as file:
                for post_url in post_urls: 
                    file.write(post_url + '\n')
            
            self.close_browser()



            # like_button = browser.find_elements_by_class_name('wpO6b')[1].click() 
            # time.sleep(2) 

            # print(f'Post {userpost} Successful')
            # self.close_browser()


my_bot = InstagramBot(username, password)
my_bot.login()
my_bot.put_exactly_like('https://www.instagram.com/p/Cde_0YcrJDa/')

