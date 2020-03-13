import requests
import json
from bs4 import BeautifulSoup


def main():
	with requests.Session() as s:
		account_info = json.load(open('..//..//Account.json'))
		header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) ""AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
		}
		logindata = {'LoginForm.LoginWithEmail': 'True', 'LoginForm.Username': account_info['CollegeData']['Email'], 'LoginForm.Email': account_info['CollegeData']['Email'], 'LoginForm.Password': account_info['CollegeData']['Password'], 'LoginForm.CanonicalUrl': '/en/explore-colleges/college-search/SearchByPreference/?SearchByPreference.SearchType=ByName&SearchByPreference.CollegeName=+', 'button': ''
		}
		p = s.post('https://www.collegedata.com/en/login/Submit/', headers=header, data=logindata)
		res = s.get('https://www.collegedata.com/en/explore-colleges/college-search/SearchByPreference/?SearchByPreference.SearchType=ByName&SearchByPreference.CollegeName=+')
	soup = BeautifulSoup(res.text, 'html.parser')
	select_school = soup.select("div.t-title__details a")	
	select_data = soup.find_all('td')[5::]
	school_amount = int(len(select_school)/3)
	SearchResult = open('CollegeData_SearchResult.txt', 'w')
	for school in range(school_amount):
		SearchResult.write('\nNumber: ' + str(school+1))
		SearchResult.write('\nhttps://www.collegedata.com' + select_school[school]['href'] + '\n')
		for vitals in range(9):
			if vitals == 1:
				continue
			SearchResult.write(select_data[(9 * school) + vitals].text.strip().replace('\n', ': ').replace('\r', ': ') + '\n')
		for financial in range(7):
			if financial == 0 or financial == 1:
				continue
			SearchResult.write(select_data[(8 * school) + financial + (9 * school_amount) + 1].text.strip().replace('\n', ': ').replace('\r', ': ')+ '\n')
		for students in range(7):
			if students == 0:
				continue
			SearchResult.write(select_data[(8 * school) + students + ((9 + 8) * school_amount) + 1].text.strip().replace('\n', ': ').replace('\r', ': ') + '\n')
	print('Finish')


if __name__ == '__main__':
	main()
