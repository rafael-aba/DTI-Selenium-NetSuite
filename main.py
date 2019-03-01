from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configparser
import time

# LOAD CONFIG
config = configparser.ConfigParser()
config.read('config.ini')

# GO TO FRONT PAGE
driver = webdriver.Chrome('/home/rafael/Documents/Selenium/chromedriver')
driver.maximize_window()
driver.set_window_position(0,0)
driver.get('https://system.netsuite.com/pages/customerlogin.jsp')

# ENTER CREDENTIALS
elem = driver.find_element_by_id('userName')
elem.clear()
elem.send_keys(config['DEFAULT']['EMAIL'])
elem = driver.find_element_by_id('password')
elem.clear()
elem.send_keys(config['DEFAULT']['PASSWORD'])
elem.send_keys(Keys.RETURN)

# ENTER SECURITY ANSWER IF NEEDED
try:
	elem = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID,'null'))) 
	elem.clear()
	elem.send_keys(config['DEFAULT']['SECURITY_ANSWER'])
	elem.send_keys(Keys.RETURN)
except:
	print("No security answer needed")

# GO TO THE PAGE WE WANT
elem = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,'Acompanhamento semanal de horas'))) 
elem.click()

# WAIT OBJECT WE WANT TO LOAD
add_button = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'timeitem_addedit'))) 

# FILL PROJECT:
# open options
elem = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="parent_actionbuttons_timeitem_customer_fs"]/a[2]'))) 
elem.click()

# click on list
elem = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID,'customer_popup_list'))) 
elem.click()

# click on element we want
elem = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,config['DEFAULT']['PROJECT']))) 
elem.click()

# GET ANY CLICKABLE ELEMENT
elem_helper = WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,'//*[@id="tr_fg_fieldGroup18"]/td[1]/table/tbody/tr/td/div/span[2]/span'))) 

# FILL DAYS
if config['DEFAULT']['MONDAY'] == 'True':
	day = WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,'//*[@id="timeitem_splits"]/tbody/tr[2]/td[6]/div'))) 
	day.click()
	day.click()
	day = WebDriverWait(driver,1).until(EC.presence_of_element_located((By.ID,'hours1'))) 
	day.send_keys(config['DEFAULT']['MONDAY_HOURS'])
	elem_helper.click()

if config['DEFAULT']['TUESDAY'] == 'True':
	day = WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,'//*[@id="timeitem_splits"]/tbody/tr[2]/td[7]/div'))) 
	day.click()
	day.click()
	day = WebDriverWait(driver,1).until(EC.presence_of_element_located((By.ID,'hours2'))) 
	day.send_keys(config['DEFAULT']['TUESDAY_HOURS'])
	elem_helper.click()

if config['DEFAULT']['WEDNESDAY'] == 'True':
	day = WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,'//*[@id="timeitem_splits"]/tbody/tr[2]/td[8]/div'))) 
	day.click()
	day.click()
	day = WebDriverWait(driver,1).until(EC.presence_of_element_located((By.ID,'hours3'))) 
	day.send_keys(config['DEFAULT']['WEDNESDAY_HOURS'])
	elem_helper.click()

if config['DEFAULT']['THURSDAY'] == 'True':
	day = WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,'//*[@id="timeitem_splits"]/tbody/tr[2]/td[9]/div'))) 
	day.click()
	day.click()
	day = WebDriverWait(driver,1).until(EC.presence_of_element_located((By.ID,'hours4'))) 
	day.send_keys(config['DEFAULT']['THURSDAY_HOURS'])
	elem_helper.click()

if config['DEFAULT']['FRIDAY'] == 'True':
	day = WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,'//*[@id="timeitem_splits"]/tbody/tr[2]/td[10]/div'))) 
	day.click()
	day.click()
	day = WebDriverWait(driver,1).until(EC.presence_of_element_located((By.ID,'hours5'))) 
	day.send_keys(config['DEFAULT']['FRIDAY_HOURS'])
	elem_helper.click()

# ADD HOURS
add_button.click()

# WAIT TO LOAD
elem = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'timeitem_row_1'))) 

# SAVE
elem = WebDriverWait(driver,1).until(EC.presence_of_element_located((By.ID,'btn_secondarymultibutton_submitter'))) 
elem.click()


loop = True
while loop :
	elem = driver.find_elements_by_class_name('listtexthl')
	for val in elem:
		if val.value_of_css_property('background-color') == 'rgba(152, 181, 227, 1)':
			print('SUCESSO!')
			loop = False
			break

driver.close()


