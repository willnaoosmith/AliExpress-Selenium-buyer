from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from time import sleep

code = "POCOX99"
cpf = "48119465881"

try:
	options = Options()
	browser = webdriver.Firefox(options=options)

	browser.get('https://login.aliexpress.com/')
	sleep(2)
	input("Aperte [Enter] após seu login")
	sleep(2)
	browser.get('https://shoppingcart.aliexpress.com/shopcart/shopcartDetail.htm')
	sleep(2)
	browser.find_elements_by_class_name('next-checkbox-input')[2].click()
	sleep(2)
	browser.find_element_by_id('checkout-button').click()
	sleep(3)
	browser.find_element_by_xpath("//*[@class='next-btn next-medium next-btn-primary next-btn-text selected-payment-btn']").click()
	sleep(0.5)
	
	try:
		browser.find_element_by_xpath("//*[@class='pay-title otc-boleto']").click()
	
	except:
		browser.find_element_by_xpath("//*[@class='pay-title boleto']").click()

	sleep(0.5)
	browser.find_element_by_id('cpfNo').send_keys(cpf)
	sleep(0.5)
	browser.find_elements_by_xpath("//*[@class='next-btn next-large next-btn-primary']")[2].click()
	sleep(1)

	while True:
		browser.find_element_by_id('code').send_keys(code)
		sleep(0.1)
		browser.find_element_by_xpath("//*[@class='next-btn next-small next-btn-secondary']").click()
		sleep(0.9)
		
		try:
			if browser.find_element_by_xpath("//*[@class='next-balloon next-balloon-normal next-balloon-medium next-balloon-top-right next-overlay-inner']/span").text != "Insira um código promocional válido.": 
				break

		except Exception as error:
			pass

	sleep(0.5)

	browser.find_element_by_id('checkout-button').click()

except Exception as error:
	print(error)
	input("exit")
	#browser.close()

finally:
	browser.close()