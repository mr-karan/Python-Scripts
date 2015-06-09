import re
from mechanize import Browser
from bs4 import BeautifulSoup

def parsedata(content):
	soup=BeautifulSoup(content)
	text=soup.get_text()
	begin = text.index('Roll')
	end = text.index('Check')
	return text[begin:end].encode('UTF-8').strip()


def submitmethod(roll):
	br = Browser()
	br.open("http://cbseresults.nic.in/class12/cbse122015_all.htm")
	br.select_form(name="FrontPage_Form1")
	br["regno"] = str(roll) 
	response = br.submit()  
	content = response.read()
	return parsedata(content)

def main():
	results = [submitmethod(num) for num in range(1600001,1600005)]
	f = open('result.txt', 'w')
	for i in results:
		f.write(i)
	f.close()

if __name__ == '__main__':
	main()






"""
1600001 till 1719685

2600001 till 2764100

3600001 till 3647565

4600001 till 4652913

5600001 till 5691383

5800001 till 5917335

6600001 till 6648925

7600001 till 7682109

9100001 till 9209884

9600001 till 9770351

"""
