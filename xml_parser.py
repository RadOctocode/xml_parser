from xml.dom import minidom
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime


mydoc = minidom.parse('example.xml')

ip_add = mydoc.getElementsByTagName('IP_Address')
time_stamp = mydoc.getElementsByTagName('TimeStamp')
print(ip_add[0].firstChild.data)

split_time=(time_stamp[0].firstChild.data).replace("T", " ")
print(split_time)
split_time=(split_time).replace("Z", "")
d2 = datetime.datetime.strptime(split_time, "%Y-%m-%d %H:%M:%S")

print(d2-datetime.timedelta(hours=5))#prints out time stamp 5 hours before

#driver sample code
driver = webdriver.Firefox()
driver.get("https://binghamton.splunkcloud.com/en-US/account/login?return_to=%2Fen-US%2F")
username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")


username.send_keys("mtan23")#put in username
password.send_keys("1vyisAspy")#put in password


login_attempt = driver.find_element_by_xpath("//*[@type='submit']")
login_attempt.submit()

#driver.find_element_by_xpath('//a[@href="'+"Search & Reporting"+'"]').click()
driver.find_element_by_xpath().click()

continue_link = driver.find_element_by_link_text("Search & Reporting")
continue_link.click();









#driver.close()
#end of driver sample code

#click this button 
#<div class="app" data-appid="search" style="background-color:#65A637">	                    <a href="/en-US/app/search/">	                            <span class="helper"></span><img src="/en-US/splunkd/__raw/servicesNS/mtan23/search/static/appIcon.png">	                        <div class="app-name">Search &amp; Reporting</div>	                        <div class="drag-handle"></div>	                        	                    </a>	                </div>


#resources               
#http://www.thetaranights.com/login-to-a-website-using-selenium-python-python-selenium-example/
#https://pythonspot.com/selenium-click-button/
#http://selenium-python.readthedocs.io/locating-elements.html#locating-by-xpath

