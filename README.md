# Moodle Student Data Scraper
The purpose of this software is to extract participants data from Moodle and save it on a table file.

_**Note:** Only tested in Moodle 3.7 using Boost Theme_
_**Note 2:** This application may not work in all Moodles. In reason of that, you are free to modify it to attend your purposes_

**Scraped Data**
1. Participants name
2. Participants email
3. Participants access frequency per day
4. Participants assignments grade
5. Participants assignments finishing date

**What you need**
* Python3
* Selenium
   * You can download it by using `pip3 install selenium`
* Chrome
* Right chromedriver for your chrome version:
   * You can download chromedriver here: https://sites.google.com/a/chromium.org/chromedriver/downloads 
   * You can check your chrome version by typing the following 'url' on your chrome: `chrome://version`
   * Put it inside project's main directory

**How to use it**
1. Clone this repository by using: `git clone https://github.com/nickolasrm/moodle-student-data-scraper`
2. Open the file data.cfg on a text editor of your preference
3. Put required data
   * Username: `username = your_moodle_username`
   * Password: `password = your_moodle_password`
   * Course: `course = My Course Name`
   * URL: `url = http://your_moodle.com`
   * chromedriver: `chromedriver = ./chromedriver_file`
   * Roles Filter: `participantsFilter = roles_combobox_option_text`
4. (Optional) Select data you want to extract by putting `yes` or `no` on the options under targets section in `data.cfg` file.
5. Save it
6. In project's main folder, run the following command `python3 start.py`
7. The scraped data is saved on a file named `__outputStudentData.csv`, you can open it on any sheet reader using:  you want (e.g., LibreOffice Calc).
