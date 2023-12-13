import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import urllib
global wait
chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#the initial URLs in "links.txt" end "#tab=summary", then to get the cast tab it must be changed to "#tab=cast-and-crew" for all links. You may use Word for it, then save it as another txt file.
#also, by using initial URLs, you can write codes to navigate between tabs and reach the cast tab (but I think using Word is easier :) )
with open("urls_casts.txt", "r", encoding="utf-8") as urls:
    graph_info = []
    for url in urls:
        driver.get(url)

        driver.maximize_window() 
        driver.implicitly_wait(10) 
        
        actors = []
        movie = driver.find_element(By.TAG_NAME, "h1").get_attribute("innerHTML")
        
        table = driver.find_element(By.XPATH, "//*[@id='cast-and-crew']/div[1]/table") #leading cast table
        rows =table.find_elements(By.TAG_NAME, 'tr') #there may be more than one actor in the table
        
        try:
            for row in rows:

                link = row.find_element(By.TAG_NAME, "a")
                href = link.get_attribute("href")
                actors.append(href)

            for i in actors: 

                driver.get(i) #go to actor page
                driver.implicitly_wait(10)
                actor = driver.find_element(By.TAG_NAME, "h1").get_attribute("innerHTML")
                
# The main purpose is to get the actor's popularity in the regarding year, but there is only a graph showing that data and it is not possible to scrap from graph.
# However, there is a one-pixel-sized table showing that data, in iframe. To reach that data firstly you must switch to iframe.
                match = urllib.parse.urlparse(i).path.split("/")[2].split("-")[0] # to define ID of iframe
                iframe_id = "/current/cont/graphs/person-lead-records-yearly/" + match 
                iframe = driver.find_element(By.ID, iframe_id) # find the iframe in the page
                
                driver.switch_to.frame(iframe) # one-pixel-sized table can be found now :)

                table = driver.find_element(By.XPATH, "//*[@id='highest_grossing_ranking_div']/div/div[1]/div/div/table")
                # The following lines help to get data for a particular year (it is 2018 below). For other years "tr[19]" would be changed.
                year = table.find_element(By.XPATH, "//*[@id='highest_grossing_ranking_div']/div/div[1]/div/div/table/tbody/tr[19]/td[1]").get_attribute("innerHTML")
                domestic = table.find_element(By.XPATH, "//*[@id='highest_grossing_ranking_div']/div/div[1]/div/div/table/tbody/tr[19]/td[2]").get_attribute("innerHTML")
                international = table.find_element(By.XPATH, "//*[@id='highest_grossing_ranking_div']/div/div[1]/div/div/table/tbody/tr[19]/td[3]").get_attribute("innerHTML")
                world = table.find_element(By.XPATH, "//*[@id='highest_grossing_ranking_div']/div/div[1]/div/div/table/tbody/tr[19]/td[4]").get_attribute("innerHTML")

                graph_info.append(
                            {'Movie': movie,
                             'Actor': actor,
                             'Year': year,
                             'Domestic': domestic,
                             'International': international,
                             'Worldwide': world})
                driver.switch_to.default_content() #before moving to the next actor's page switch back to default
        finally:
            continue
    driver.quit()

with open('actor_popularity.csv','w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['Movie', 'Actor', 'Year', 'Domestic', 'International', 'Worldwide']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()  # Başlık satırını yaz
    for actor_popularity in graph_info:
        writer.writerow(actor_popularity)  # Verileri yaz

print("You did it!!")
