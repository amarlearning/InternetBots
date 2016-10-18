import os
from bs4 import BeautifulSoup
import urllib2

newpath = os.getcwd() + "/codechedCode" 
if not os.path.exists(newpath):
    os.makedirs(newpath)

url="http://www.codechef.com/users/amarpandey"
page = urllib2.urlopen(url)

soup = BeautifulSoup(page.read(), "html.parser")

Links = soup.find('table', {'class' :None }).find_all('a')
Links = Links[2:]

# Labels(Names) of every Question you solved!
Labels = []
for Link in Links:
	Labels.append(Link.text)

# All urls of questions you solved
solutionUrls = []
for Link in Links:
	solutionUrls.append(Link['href'])

# Navigating to Every url of the solution & get the solution code!
counter = 0
for link in solutionUrls:
	link = "http://codechef.com" + link
	page = urllib2.urlopen(link)
	soup = BeautifulSoup(page.read(), "html.parser")
	getCode = soup.find('td', {'class' : 'centered', 'width': '75'}).find_all('a')
	FileExtension = soup.find('td', {'class' : 'centered', 'width': '70'}).text
	tempString = getCode[0]['href'].replace("viewsolution", "viewplaintext")
	SourceCodeLink = "http://codechef.com" + tempString
	page = urllib2.urlopen(SourceCodeLink)
	soup = BeautifulSoup(page.read(), "html.parser")
	SourceCode = soup.find('pre', {'class' : None }).text
	filename = Labels[counter] + '.' + FileExtension
	with open(os.path.join(newpath, filename), 'wb') as temp_file:
	    temp_file.write(SourceCode)
	counter += 1