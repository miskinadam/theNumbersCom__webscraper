# theNumbersCom__webscraper
# First of all I am not a data scientist, but a marketing phd. My main job does not include coding. I am a rookie in coding and Python. So, maybe there are more simple coding ways to collect the same data.
# I have a post-doc project about movies and pre-release ewom. So, for movies, I scraped data from The-Numbers.com. 
# I had some trouble finding example codes for my project. That's why I decided to share my codes with other people who are searching for similar codes. 
# I used the Selenium library, not BeatifulSoup. I have tried both and Selenium worked but BS didn't. Maybe you can also accomplish this by BS.
# In my project, firstly on the "report builder" page of The Numbers I got the movie list (I filtered by year, and some other criteria) to get the movie page links and the data on the list.
# This list can be easily copied and pasted to Excel (no need for coding). 
# For the project, firstly movie page URLs are scraped from the report page (movie_urls.py). Then, by using these URLs, all the needed data can be scraped. 
# You can find two example files in this repository. The first one, movie_info.py, is the basic one. It can be used as a reference for any data scraping work from this website. The other one, actor_popularity.py, is more complex. It deals with a specific situation, iFrame. Data is hidden and to get it some tricky moves are required :) 
# Enjoy
