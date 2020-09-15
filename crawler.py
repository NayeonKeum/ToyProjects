from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('C://chromedriver.exe')
driver.get('https://vibe.naver.com/chart/genre-DS101')

driver.find_element_by_css_selector('#app > div.modal > div > div > a').click()
songs = []

for i in range(1, 101):
    button = driver.find_element_by_css_selector('#content > div.track_section > div:nth-child(1) > div > table > tbody > tr:nth-child('+str(i)+') > td.lyrics')
    if(button.text != ''):
        button.click()
        lyrics = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#app > div.modal > div > div > div.ly_contents > p > span:nth-child(2)'))
        )
        lyrics_data = lyrics.text.replace('\n', ' ')
        songs.append(lyrics_data)
        close = driver.find_element_by_css_selector('#app > div.modal > div > div > a')
        close.click()
    if i%10==0:
        driver.execute_script("arguments[0].scrollIntoView(true);", button)

print(songs)
