import os
from bs4 import BeautifulSoup
import urllib2

counter = 0
Labels = []
solutionUrls = []

newpath = os.getcwd() + "/codechedCode" 
if not os.path.exists(newpath):
    os.makedirs(newpath)

url="http://www.codechef.com/users/amarpandey"
page = urllib2.urlopen(url)

soup = BeautifulSoup(page.read(), "html.parser")

Links = soup.find('table', {'class' :None }).find_all('a')
Links = Links[2:]

# Labels(Names) of every Question you solved!
for Link in Links:
	Labels.append(Link.text)

# All urls of questions you solved
for Link in Links:
	solutionUrls.append(Link['href'])

# Language Extension Dictionary!
Extensions = {'C' : 'c',
			  'C++ 4.3.2' : 'cpp',
			  'PYTH' : 'py',
			  'C++ 4.9.2' : 'cpp',
			  'PYTH 3.4' : 'py',
			  'JAVA' : 'java'
			 }
# Navigating to Every url of the solution & get the solution code!
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
	filename = Labels[counter] + '.' + Extensions[FileExtension]
	with open(os.path.join(newpath, filename), 'wb') as temp_file:
	    temp_file.write(SourceCode)
	counter += 1