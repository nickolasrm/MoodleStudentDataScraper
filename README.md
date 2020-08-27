# Moodle Student Data Scraper
The purpose of this software is to extract participants data from Moodle and save it on a table file.

**Data to Scrape**
1. Participants access frequency per day
2. Participants grades

**How to use it**
1. Clone this repository by `git clone https://github.com/nickolasrm/moodle-student-data-scraper`
2. Open the file data.cfg in a text editor of your preference
3. Put required data
  * Username: `username = your_user_name@email_service.com`
  * Password: `password = your_moodle_password`
  * Course: `My Course Name`
  * URL: `url = http://your_moodle.com`
4. Save it
5. In the main folder run the following command `scrapy crawl moodle`
