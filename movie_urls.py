from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
global wait
chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://the-numbers.com/movies/report/All/All/All/All/All/All/All/All/All/0.1/None/2018/2018/None/None/None/None/None/None?show-release-date=On&show-domestic-box-office=On&show-international-box-office=On&show-worldwide-box-office=On&view-order-by=domestic-box-office&view-order-direction=desc")
urls = []

table = driver.find_element(By.XPATH, "//*[@id='page_filling_chart']/center[1]/table/tbody")

#In this example there is only one column containing links, therefore I directly find the all 'a' tags (all are movie hrefs). 
#If there are more than one link-column then a few more steps have to be added (firstly all rows must be found).
Links = table.find_elements(By.TAG_NAME, "a")
for link in Links:
    i = link.get_attribute("href")
    urls.append(i)

with open("links.txt", "a") as f:
    for url in urls:
        f.write(url + "\n")

driver.quit()
