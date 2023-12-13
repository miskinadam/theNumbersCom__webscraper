import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(ChromeDriverManager().install())

with open("links.txt", "r", encoding="utf-8") as urls:  
    Movie_Info = []
    for url in urls:
        driver.get(url)
        wait = WebDriverWait(driver, 15)
        movie = driver.find_element(By.TAG_NAME, "h1").get_attribute("innerHTML") #get the name of the movie
        
        table = driver.find_element(By.XPATH, "//*[@id='summary']/table[3]") #find the table containing the needed data 
        mpaa = table.find_element(By.XPATH, "//*[@id='summary']/table[3]/tbody/tr[4]/td[2]/a").get_attribute("innerHTML")
        source = table.find_element(By.XPATH, "//*[@id='summary']/table[3]/tbody/tr[9]/td[2]/a").get_attribute("innerHTML")
        creative_type = table.find_element(By.XPATH, "//*[@id='summary']/table[3]/tbody/tr[12]/td[2]/a").get_attribute("innerHTML")
        prod_comp = table.find_element(By.XPATH, "//*[@id='summary']/table[3]/tbody/tr[13]/td[2]/a").get_attribute("innerHTML")
        Movie_Info.append(
            {'Movie': movie,
             'MPAA_Rating': mpaa,
             'Source': source,
             'Creative_Type': creative_type,
             'Production/Financing_Comp.': prod_comp})

    driver.quit()
#to save the data in a csv file
with open('movie_info.csv', 'w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['Movie', 'MPAA_Rating', 'Source', 'Creative_Type', 'Production/Financing_Comp.']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()  
    for movie_info in Movie_Info:
        writer.writerow(movie_info)  





