# Moodle Student Data Scraper
The purpose of this software is to extract participants data from Moodle and save it on a table file.

_**Note:** Only tested in Moodle 3.7 using Boost Theme_

**Data to Scrape**
1. Participants access frequency per day
2. Participants grades

**What you need**
* Python3
* Selenium
   * You can download it by using `pip3 install selenium`
* Chrome
* Chrome driver for your chrome version
   * You can download chrome driver here: https://sites.google.com/a/chromium.org/chromedriver/downloads 
   * You can check your chrome version by typing the url `chrome://version`
   * Put it inside project main directory

**How to use it**
1. Clone this repository by `git clone https://github.com/nickolasrm/moodle-student-data-scraper`
2. Open the file data.cfg in a text editor of your preference
3. Put required data
   * Username: `username = "your_moodle_username"`
   * Password: `password = "your_moodle_password"`
   * Course: `course = "My Course Name"`
   * URL: `url = "http://your_moodle.com"`
   * driver: `driver = chromedriver_file`
4. Save it
5. In the main folder run the following command `scrapy crawl moodle`
