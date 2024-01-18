import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import urllib


image_search_query = [
    "toyota+RAV4",
    "toyota+86",
    "toyota+Sienna",
    "toyota+Camry",
    "toyota+C-HR",
    "toyota+Corolla+sedan",
    "toyota+4Runner",
    "toyota+Venza"
]

views = {
    'stock+photos' : 20,
    "front+view" : 20,
    "side+profile" : 20,
    "back+angle+view" : 20,
    "on+the+road" : 20,
    "tailight+view+photoshoot" : 20,
    "headlight+view+photoshoot" : 20,
    "modifications+photoshoot" : 20
    }

driver_path = "/Users/a970/Downloads/chromedriver/chromedriver"
counter = 0
for car_model in image_search_query:
    for angle, numOfPics in views.items():
        options = webdriver.ChromeOptions()
        options.add_argument('--user-data-dir=/Users/a970/Library/Application Support/Google/Chrome/Default')
        driver = uc.Chrome(options=options)
        driver.minimize_window()

        url = 'https://www.google.com/search?q={0}+{1}&hl=en&tbm=isch&sxsrf=APwXEdeMCCcn15mo1obWv-xVcr_tpnFYQg%3A1684476865544&source=hp&biw=1737&bih=1032&ei=wRNnZNX-HtX4kPIP9umT2AY&iflsig=AOEireoAAAAAZGch0VXQnHgSIAIKBwcg5h0gf-nJjQvD&oq=toyota+supr&gs_lcp=CgNpbWcQAxgAMgQIIxAnMgQIIxAnMggIABCABBCxAzIICAAQgAQQsQMyBQgAEIAEMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQM6BwgjEOoCECc6CAgAELEDEIMBOgQIABADOgkIABAYEIAEEApQlglY7SNgpSxoB3AAeAGAAZIBiAHkDJIBBDEwLjeYAQCgAQGqAQtnd3Mtd2l6LWltZ7ABCg&sclient=img'.format(car_model, angle)
        driver.get(url)
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

        time.sleep(5)


        img_results = driver.find_elements(By.XPATH, "//img[contains(@class, 'Q4LuWd')]")

        image_urls = []
        for img in img_results:
            image_urls.append(img.get_attribute('src'))

        folderPath = '/Users/a970/Documents/DatasetStorage/'
        modifiedFileName = car_model.replace("+", "_")

        for i in range(numOfPics):
            urllib.request.urlretrieve(str(image_urls[i]), folderPath + "{0} {1}.jpg".format(modifiedFileName, i + counter))

        driver.quit()
        time.sleep(3)
        counter += numOfPics
        




