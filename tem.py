import time
from lxml import html
import requests
from selenium import webdriver
data= webdriver.Firefox()
url="https://dz.openfoodfacts.org/"
data.get(url)
j=data.find_elements_by_class_name("list_product_a")
t=set()
for elem in j:
	t.add(elem.get_attribute('href'))
	t.add(elem.find_element_by_class_name("list_product_name").text)
print(len(t))			
for x in range(2,20):
	url="https://dz.openfoodfacts.org/"+str(x)
	data.quit()
	data= webdriver.Firefox()
	data.get(url)
	j=data.find_elements_by_class_name("list_product_a")
	t=set()
	for elem in j:
		t.add(elem.get_attribute('href'))
		t.add(elem.find_element_by_class_name("list_product_name").text)

print(len(t))
print(t)