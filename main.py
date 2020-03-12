import requests
from bs4 import BeautifulSoup
'''
def getCookie():
	header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) "
"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
	}
	logindata = {'LoginForm.LoginWithEmail': 'True', 'LoginForm.Username': 'jp6ru8958958@gmail.com', 'LoginForm.Email': 'jp6ru8958958@gmail.com', 'LoginForm.Password': 'cd958958', 'LoginForm.CanonicalUrl': '/en/explore-colleges/college-search/SearchByPreference/?SearchByPreference.SearchType=ByName&SearchByPreference.CollegeName=+', 'button': ''
	}
	r = requests.get('https://www.collegedata.com/en/explore-colleges/college-search/SearchByPreference/?SearchByPreference.SearchType=ByName&SearchByPreference.CollegeName=+', headers=header, data=logindata)

	return cookie
'''

def main():
	header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) "
"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
	}
	logindata = {'LoginForm.LoginWithEmail': 'True', 'LoginForm.Username': 'jp6ru8958958@gmail.com', 'LoginForm.Email': 'jp6ru8958958@gmail.com', 'LoginForm.Password': 'cd958958', 'LoginForm.CanonicalUrl': '/en/explore-colleges/college-search/SearchByPreference/?SearchByPreference.SearchType=ByName&SearchByPreference.CollegeName=+', 'button': ''
	}
	with requests.Session() as s:
		p = s.post('https://www.collegedata.com/en/login/Submit/', headers=header, data=logindata)
		r = s.get('https://www.collegedata.com/en/explore-colleges/college-search/SearchByPreference/?SearchByPreference.SearchType=ByName&SearchByPreference.CollegeName=+')
	'''
	fp = open('collegedata2.txt', 'w')
	fp.write(r.text)
	fp.close()
	r = open('collegedata2.txt', 'r')
	'''
	soup = BeautifulSoup(r.text, 'html.parser')
	sel_school = soup.select("div.t-title__details a")
	
	school_amount = int(len(sel_school)/3)
	
	sel_data = soup.find_all('td')[5::]
	wr = open('collegedata_print.txt', 'w')

	for school in range(school_amount):
		wr.write('\nNumber: ' + str(school+1))
		wr.write('\nhttps://www.collegedata.com' + sel_school[school]['href'] + '\n')
		for vitals in range(9):
			if vitals == 1:
				continue
			wr.write(sel_data[(9 * school) + vitals].text.strip().replace('\n', ': ').replace('\r', ': ') + '\n')
		for financial in range(7):
			if financial == 0 or financial == 1:
				continue
			wr.write(sel_data[(8 * school) + financial + (9 * school_amount) + 1].text.strip().replace('\n', ': ').replace('\r', ': ')+ '\n')
		for students in range(7):
			if students == 0:
				continue
			wr.write(sel_data[(8 * school) + students + ((9 + 8) * school_amount) + 1].text.strip().replace('\n', ': ').replace('\r', ': ') + '\n')
	print('finish')

if __name__ == '__main__':
	main()