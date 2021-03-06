# 크롤링 라이브러리
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 텍스트 분석 라이브러리
import matplotlib.pyplot as plt
import nltk
from konlpy.tag import Okt
from wordcloud import WordCloud

# 텍스트 클라우드 모양 변경 라이브러리
import numpy as np
from PIL import Image

driver = webdriver.Chrome('C://chromedriver.exe')
driver.maximize_window()
driver.get('https://vibe.naver.com/chart/total')

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


# 마스크 생성
mask = np.array(Image.open("all.png"))

font_path = r'c://windows/fonts/malgun.ttf'
wordcloud = WordCloud(font_path = font_path, background_color='white', mask = mask,  width = 800, height = 800)

t = Okt()
token_ko = []

# 각 노래 별 명사 추출
for text in songs:
    token_ko += t.nouns(text)

print(token_ko)

# 한 자리 수 단어 제거
for i, v in enumerate(token_ko):
    if len(v) < 2:
        token_ko.pop(i)

print(token_ko)

ko = nltk.Text(token_ko, name = "바이브 차트 텍스트 클라우드")
# 상위 단어 100 선정
most_nouns = ko.vocab().most_common(100)

# 워드 클라우드 생성
wordcloud = wordcloud.generate_from_frequencies(dict(most_nouns))


# 표 그림
fig = plt.figure(figsize=(7,7))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
