import re
from mechanize import Browser
from bs4 import BeautifulSoup
import csv


def parsedata(content):
	soup = BeautifulSoup(content)
	result = soup.find("table", border=1)
	rows = result.find_all('tr')
	subjectname=[]
	markall=[]
	#details = {}
	#name=[]
	#marks=[]
	with open('try.csv','a') as f:
		csvwriter = csv.writer(f)
		for row in rows[:9]:
			col=row.findAll('td')
			sub=col[1].text.encode('utf-8')
			subjectname.append((sub))

			marks=col[4].text.encode('utf-8')
			markall.append((marks))
		csvwriter.writerows([subjectname,])
		csvwriter.writerows([markall,])
				#subjectname.append((sub))


			#subject['marks'].append(col[4].text.encode('utf-8'))
			#print subject['marks']
			#markall.append((marks))
			#marks.append(subject)
		#print marks
			#print marks
			#csvrow+=subject["code"]+","+subject["marks"]+","
		#print csvrow
		# print sub,marks
		#fieldnames=['name','marks']
		#writer = csv.DictWriter(f, fieldnames=fieldnames)

		#writer.writerow(details)

		#csvwriter.writerows(details['name'],)
		#csvwriter.writerows(details['marks'],)

			#print sub,marks




	# subCode=col[1].text.encode('utf-8')
	# subCode=
	# cells = [c.text.encode('utf-8') for c in row.findAll('td')]
	# print cells
	# csvwriter.writerow(cells)


def submitmethod(roll):
	br = Browser()
	br.open("http://cbseresults.nic.in/class12/cbse122015_all.htm")
	br.select_form(name="FrontPage_Form1")
	br["regno"] = str(roll)
	response = br.submit()
	content = response.read()
	return parsedata(content)


def main():
	for i in range(1600001, 1600010):
		print "AT Roll %d" % i
		submitmethod(i)

	# print
	'''f = open('result.txt', 'w')
    for i in results:
        f.write(i)
    f.close()
    '''


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
