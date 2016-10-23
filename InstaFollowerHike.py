# Importing all library that are used!
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

def main():
# Yeah, I know it consumes a lot of RAM.
# But still i don't know why i always use this.
	driver = webdriver.Chrome()

# Yes, an INSTAGRAM follower bot.
	driver.get("https://www.instagram.com")

# Resizing the window so that you can see what's going on!
	driver.maximize_window()

# It will open a signup page, so we redirect to login page.
	Redirect_Login = driver.find_element_by_link_text('Log in')
	driver.implicitly_wait(5)
	Redirect_Login.click()

# Yes, we need your Instagram username && Password.
# You we can modify to make it user input type.
# But you know i am too lazy to do that.
	instagram_username = "iamarpandey"
	instagram_password = "***********"

# Getting the username and password's Xpath
# you know we have to enter the credentials, that's why!
	username_xpath = "//*[@id=\"react-root\"]/section/main/article/div[2]/div[1]/div/form/div[1]/input"
	password_xpath = "//*[@id=\"react-root\"]/section/main/article/div[2]/div[1]/div/form/div[2]/input"

# Getting the Login Button Xpath and Search bar Xpath.
	login_button_xpath = "//*[@id=\"react-root\"]/section/main/article/div[2]/div[1]/div/form/span/button"
	search_xpath = "//*[@id=\"react-root\"]/section/nav/div/div/div/div[1]/input"

# Getting the followers and follwing button Xpath.
# Don't worry will i will not make any mess.
	followers_xpath = "//*[@id=\"react-root\"]/section/main/article/header/div[2]/ul/li[2]/a"
	following_xpath = "//*[@id=\"react-root\"]/section/main/article/header/div[2]/ul/li[3]/a"

# Getting the Xpath of First search result of dropdown.
	dropdown_xpath = "//*[@id=\"react-root\"]/section/nav/div/div/div/div[1]/div[2]/div[2]/div/a[1]/div/div[1]/span"

# I need this for the scrolling of users!
	scroll_xpath = "/html/body/div[2]/div/div[2]/div/div[2]"

# Trying to focus on username and password, so that i can enter the credentials.
	username_field_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(username_xpath))
	password_field_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(password_xpath))

# Trying ot focus on Login button as well, we need this later!
	login_button_field_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(login_button_xpath))

# Clearing of the username and password feild!
	username_field_element.clear()
	username_field_element.send_keys(instagram_username)
	password_field_element.clear()
	password_field_element.send_keys(instagram_password)

# And here we go, BOOM your account is here!
# Let's began the process.
	login_button_field_element.click()


# Search for a Verified profile to follow as many people as we want!
	search_field_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(search_xpath))
	search_field_element.send_keys("ipoonampandey")

# We need to wait for sometime, as it's performing the search.
	driver.implicitly_wait(5000)

# Selecting the result one for the search result.
	dropdown_field_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(dropdown_xpath))
	dropdown_field_element.click()

# Looking onto all the people that follow this verified profile.
	followers_field_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(followers_xpath))
	followers_field_element.click()

# Defining some of the variables that will be used during that whole following process!
	run_script = False
	i = 1
	j = 1

# Start clicking follow button, stop when you don't find one!
	while not run_script:
		follow_xpath = "/html/body/div[2]/div/div[2]/div/div[2]/ul/li["+str(i)+"]/div/div[2]/span/button"
		follow_field_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(follow_xpath))
		follow_field_element.click()
		driver.implicitly_wait(15)
		centerPanel = driver.find_element_by_css_selector("body > div:nth-child(9) > div > div._g1ax7 > div > div._4gt3b")
		
	# This was the hard part, scroll down. the content is loaded with AJAX.
	# Yeah, I know Javascript is awesome. It again helped me.
		jsScript = """
	        function move_down(element) {
	            element.scrollTop = element.scrollTop + 50;
	        }

	        move_down(arguments[0]);
	        """
		driver.execute_script(jsScript, centerPanel)
		while j < 10000000 :
			j = j + 1
		i = i + 1
		j = 1 

# It's time to close this, lot of work is done today! 
	driver.close()

# I am the one who controls all this, Hell yeah!
if __name__ == '__main__':
	main()