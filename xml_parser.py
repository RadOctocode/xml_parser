from xml.dom import minidom
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime


mydoc = minidom.parse('example.xml')

ip_add = mydoc.getElementsByTagName('IP_Address')
time_stamp = mydoc.getElementsByTagName('TimeStamp')
print('IP:')  
print(ip_add[0].firstChild.data)

split_time=(time_stamp[0].firstChild.data).replace("T", " ")
print(split_time)
split_time=(split_time).replace("Z", "")
d2 = datetime.datetime.strptime(split_time, "%Y-%m-%d %H:%M:%S")

print(d2-datetime.timedelta(hours=5))#prints out time stamp 5 hours before

#driver sample code
driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
#end of driver sample code

#seprarte at T and find the last letter and adjust
#+- 2 hours
#all item attributes
#print('\nAll attributes:')  
#for elem in items:  
#        print(elem.attributes['name'].value)

# one specific item's data
#print('\nItem #2 data:')  
#print(items[1].firstChild.data)  
#print(items[1].childNodes[0].data)

# all items data
#print('\nAll item data:')  
#for elem in items:  
#	print(elem.firstChild.data)
                
