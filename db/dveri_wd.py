from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://dveribelorussii.com.ua')

driver.implicitly_wait(120)

driver.maximize_window()

zamer_form = driver.find_element_by_xpath("//header/div[1]//a[2]").click()

phone_input = driver.find_element_by_xpath("//*[@id='myFeedback4']//form/div[2]/input").send_keys("+380111111111")

city_input = driver.find_element_by_xpath("//*[@id='myFeedback4']/*//form/div[3]/input").send_keys("Тест")

zamer_button = driver.find_element_by_xpath("//*[@id='zamer_send']").click()

Parent_window = driver.window_handles()



driver.find_element_by_xpath(".//*[@id='myFeedback4']/div/div/div[3]/div[1]/a").click()



#message = driver.find_element_by_xpath("//*[contains(text(),'Спасибо, что обратились к нам')]").is_displayed()

driver.close()

