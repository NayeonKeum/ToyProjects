from selenium import webdriver

driver = webdriver.Chrome('C:/chromedriver.exe')
driver.get("https://solux.tistory.com")
blog = driver.find_element_by_xpath("//*[@id=\"gnb\"]/ul/li[4]/a")
blog.click()
post = driver.find_element_by_xpath("//*[@id=\"content\"]/div[2]/div[1]/a/span[2]")
post.click()
myname = driver.find_element_by_name("name")
myname.send_keys("금나연")
pw = driver.find_element_by_name("password")
pw.send_keys("rmaskdus123")
text = driver.find_element_by_css_selector("#entry12Comment > div > form > div > textarea")
text.send_keys("너무 쉽고 알찬 강의였어요! 무엇보다 응용하기 편하다는 점이 가장 좋았습니다! 감사합니다:)")
button = driver.find_element_by_class_name("btn")
button.click()
