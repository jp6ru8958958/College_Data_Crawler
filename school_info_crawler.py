import requests
from bs4 import BeautifulSoup

def main():
	'''
	url = 'https://www.collegedata.com/college/Abilene-Christian-University/?tab=profile-admission-tab'
	r = requests.get(url)
	'''
	fr = open('school_info.txt', 'r')
	soup = BeautifulSoup(fr, 'html.parser')
	sel_field = soup.find_all('dt')
	sel_data = soup.find_all('dd')
	fw = open('school_info_print.txt', 'w')
	for info in range(len(sel_field)):
		print(info+1)
		print(sel_field[info].text + ' = ' + sel_data[info].text)
		# 33


if __name__ == '__main__':
	main()
