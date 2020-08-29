from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import urllib

def getMoodleLoginURL(url):
    return urllib.parse.urljoin(url, '/moodle/login/index.php')

def getMoodleMyURL(url):
    return urllib.parse.urljoin(url, '/moodle/my')

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

def getParticipantsLinkList(driver, url, course, filter):
    driver.get(getMoodleMyURL(url))
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

def scrapeDaysData(driver, link):
    driver.get(getAllAccessURL(link))
    enableDaysTable(driver)
    data = [value.get_attribute('innerText') for value
        in driver.find_elements_by_xpath("//div[@class='chart-table-data']/table/tr/td")]
    data.pop(0)
    return data

def scrapeAssignmentsData(driver, participant_link):
    driver.get(getReportURL(participant_link))
    grades = [grade.get_attribute('innerText') for grade 
        in driver.find_elements_by_class_name('column-grade')]
    grades.pop(-1)
    grades.pop(0)
    return grades

def scrapeStudentName(driver, link):
    driver.get(link)
    return driver.find_element_by_tag_name('h2').get_attribute('innerText')

def scrapeStudentEmail(driver, link):
    driver.get(link)
    return driver.find_element_by_xpath(
        "//dd//a[contains(@href, 'mailto')]").get_attribute('innerText')

def scrapeParticipantData(driver, participant_link, targets):
    data = []
    if targets['name']:
        data.append(scrapeStudentName(driver, participant_link))
    if targets['email']:
        data.append(scrapeStudentEmail(driver, participant_link))
    if targets['days']:
        data.extend(scrapeDaysData(driver, participant_link))
    if targets['assignments']:
        data.extend(scrapeAssignmentsData(driver, participant_link))
    #if targets['assignments_finishing_date']:
        #data.extend(scrapeAssignmentsFinishingDateData(driver, participant_link))

    return data






def scrapeDaysHeader(driver, link):
    driver.get(getAllAccessURL(link))
    enableDaysTable(driver)
    headers = [header.get_attribute('innerText') for header 
        in driver.find_elements_by_xpath("//div[@class='chart-table-data']/table/tr/th")]
    headers.pop(0)
    return headers

def scrapeAssignmentsHeader(driver, participant_link):
    driver.get(getReportURL(participant_link))
    headers = [grade.get_attribute('innerText') for grade 
        in driver.find_elements_by_class_name('gradeitemheader')]
    headers.pop(-1)
    return headers

def scrapeHeaders(driver, participant_link, targets):
    headers = []
    if targets['name']:
        headers.append('Name')
    if targets['email']:
        headers.append('Email')
    if targets['days']:
        headers.extend(scrapeDaysHeader(driver, participant_link))
    if targets['assignments']:
        headers.extend(['Grade of "%s"' % header for header 
            in scrapeAssignmentsHeader(driver, participant_link)])
    if targets['assignments_finishing_date']:
        headers.extend(['Finishing date of "%s"' % header for header 
            in scrapeAssignmentsHeader(driver, participant_link)])

    return headers






def scrape(config):
    print('Loggin in...')

    driver = getDriver(config['chromedriver'])
    assert login(driver, config['url'], config['username'] \
        , config['password']), 'Wrong username or password'

    print('Logged!')
    print('Scraping...')

    participants = getParticipantsLinkList(driver, config['url'], 
        config['course'], config['filter'])

    data = []
    #for link in participants:
    #    data.append(scrapeParticipantData(driver, link, config['targets']))
    data.append(scrapeParticipantData(driver, participants[0], config['targets']))
    data.append(scrapeParticipantData(driver, participants[1], config['targets']))

    headers = scrapeHeaders(driver, participants[0], config['targets'])

    print('Scraping finished!')

    return {'headers': headers, 'data': data}
        
    