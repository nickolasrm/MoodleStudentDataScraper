# Moodle Student Data Scraper
The purpose of this software is to extract participants data from Moodle and save it on a table file.

_**Note:** Only tested in Moodle 3.7 using Boost Theme_
_**Note 2:** This application may not work in all moodles. In reason of that, you are free to modify this to attend your purposes_

**Scraped Data**
1. Participants names
2. Participants access frequency per day
3. Participants grades

**What you need**
* Python3
* Selenium
   * You can download it by using `pip3 install selenium`
* Chrome
* Chrome driver for your chrome version
   * You can download chrome driver here: https://sites.google.com/a/chromium.org/chromedriver/downloads 
   * You can check your chrome version by typing the url: `chrome://version`
   * Put it inside project's main directory

**How to use it**
1. Clone this repository by `git clone https://github.com/nickolasrm/moodle-student-data-scraper`
2. Open the file data.cfg on a text editor of your preference
3. Put required data
   * Username: `username = your_moodle_username`
   * Password: `password = your_moodle_password`
   * Course: `course = My Course Name`
   * URL: `url = http://your_moodle.com`
   * chdromedriver: `driver = ./chromedriver_file`
   * Filter: `participantsFilter = roles_combobox_option_text`
4. Save it
5. In the main folder run the following command `python3 start.py`
6. The scraped data is saved on a file named `__outputStudentData.csv`, you can open it on any Sheet reader app you want (e.g., LibreOffice Calc).
