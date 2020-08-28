from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import urllib
import asyncio
import time

def getMoodleLoginURL(url):
    return urllib.parse.urljoin(url, '/moodle/login/index.php')

def getAllAccessURL(url):
    return url.replace('user/view.php', 'report/log/user.php') + '&mode=all'

def getReportURL(url):
    courseId = url.split('course=')[1]
    studentId = url.split('id=')[1].split('&')[0]
    newLink = url.split('user/')[0] + \
        'grade/report/user/index.php?id=%s&userid=%s' % (courseId, studentId)
    return newLink

def getDriver(driver):
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(driver, options=op)
    driver.implicitly_wait(10)
    return driver

def login(driver, url, user, password):
    driver.get(getMoodleLoginURL(url))
    driver.find_element_by_id('username').send_keys(user)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('loginbtn').click()
    return True

def getParticipantsLinkList(driver, course, filter):
    driver.find_element_by_link_text(course).click()
    driver.find_element_by_xpath("//aside[@data-block='participants']//a").click()
    selector = Select(driver.find_element_by_xpath("//form[@id='rolesform']/select"))
    selector.select_by_visible_text(filter)
    driver.find_element_by_xpath("//div[@id='showall']/a").click()

    participants = [link.get_attribute('href') for link 
        in driver.find_elements_by_xpath("//tr//td[@class='cell c2']//a")]

    return participants

def enableDaysTable(driver):
    driver.execute_script("""
        let el = document.getElementsByClassName('chart-table-data')[0];
        el.style.display = 'block';
        el.setAttribute('aria-expanded', 'true');
        """)

def scrapeDaysHeader(driver, link):
    driver.get(getAllAccessURL(link))
    enableDaysTable(driver)
    headers = [header.get_attribute('innerText') for header 
        in driver.find_elements_by_xpath("//div[@class='chart-table-data']/table/tr/th")]
    headers.pop(0)
    return headers

def scrapeDaysData(driver, link):
    driver.get(getAllAccessURL(link))
    enableDaysTable(driver)
    data = [value.get_attribute('innerText') for value
        in driver.find_elements_by_xpath("//div[@class='chart-table-data']/table/tr/td")]
    data.pop(0)
    return data

def scrapeGradesHeader(driver, participant_link):
    driver.get(getReportURL(participant_link))
    headers = [grade.get_attribute('innerText') for grade 
        in driver.find_elements_by_class_name('gradeitemheader')]
    headers.pop(-1)
    return headers

def scrapeGradesData(driver, participant_link):
    driver.get(getReportURL(participant_link))
    grades = [grade.get_attribute('innerText') for grade 
        in driver.find_elements_by_class_name('column-grade')]
    grades.pop(-1)
    grades.pop(0)
    return grades

def scrapeStudentName(driver, link):
    driver.get(link)
    return driver.find_element_by_tag_name('h2').get_attribute('innerText')

def scrapeParticipantData(driver, participant_link):
    return {'name': scrapeStudentName(driver, participant_link),
            'days': scrapeDaysData(driver, participant_link),
            'grades': scrapeGradesData(driver, participant_link)}

def scrape(config):
    print('Loggin in...')

    driver = getDriver(config['chromedriver'])
    assert login(driver, config['url'], config['username'] \
        , config['password']), 'Wrong username or password'

    print('Logged!')

    participants = getParticipantsLinkList(driver, config['course'],
        config['filter'])
    data = []

    print('Scraping...')

    for link in participants:
        data.append(scrapeParticipantData(driver, link))

    headers = {'name' : 'Name',
                'days': scrapeDaysHeader(driver, participants[0]),
                'grades': scrapeGradesHeader(driver, participants[0])}

    print('Scraping finished!')

    return {'headers': headers, 'data':data}
        
    