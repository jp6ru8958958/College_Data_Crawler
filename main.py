import requests
import json
import csv
from bs4 import BeautifulSoup

def save_data(data_list, data, pos):
	try:
		data_list[pos] = data.text
	except:
		data_list[pos] = data
	return pos+1

def write_result_as_file( data_list, name):
        # Write soup select/find's result as a txt file for testing.
	wr = open(name, 'w')
	for i in range(len(data_list)):
		wr.write(str(i)+'\n')
		wr.write(data_list[i].text+'\n\n')

def set_field(csvWriter):
        #Only need run one time.
        field_file = open('csvField.txt', 'r')
        field_data = field_file.read().split('\n')
        csvWriter.writerow(field_data)
        field_file.close()

def set_data(csvWriter, url, data, save_pos):
	print(data[0])
	school_info_html = requests.get('https://www.collegedata.com'+url)
	soup = BeautifulSoup(school_info_html.text, 'html.parser')
	sel_p = soup.find_all('p')[64::]
	sel_b = soup.find_all('b')
	sel_a = soup.select('a')
	sel_dd = soup.find_all('dd')[33::]
	sel_td = soup.find_all('td')[5::]
	sel_tr = soup.find_all('tr')
	sel_span = soup.find_all('span')
	sel_statbar = soup.select('.statbar__item')
	sel_ul = soup.select('ul.list--nice')
	overview_intro = soup.select('p.h6.mb-4')
	save_pos = save_data(data, overview_intro[0].text.replace('\n', ''), save_pos)
	overview_intro_webLink = soup.select('p.h6 a')
	try:
		save_pos = save_data(data, overview_intro_webLink[0]['href'], save_pos)
	except:
		save_pos = save_data(data, '', save_pos)
	save_pos = save_data(data, sel_statbar[0].text.replace('\n', ''), save_pos)
	if sel_statbar[1].text.replace('\n', '')[0].isdigit():
		save_pos = save_data(data, '', save_pos)
	else:
		save_pos = save_data(data, sel_statbar[1].text.replace('\n', ''), save_pos)
	save_pos = save_data(data, sel_span[40].text, save_pos)
	try:
		save_pos = save_data(data, sel_b[0].text + sel_span[42].text.replace(' Women', ''), save_pos)
	except:
		save_pos = save_data(data, 'Not reported' + sel_span[42].text.replace(' Women', ''), save_pos)
	try:
		save_pos = save_data(data, sel_b[1].text + sel_span[43].text.replace(' Men', ''), save_pos)
	except:
		save_pos = save_data(data, 'Not reported' + sel_span[42].text.replace(' Women', ''), save_pos)
	save_pos = save_data(data, sel_span[44].text.replace('\n', ''), save_pos)
	save_pos = save_data(data, sel_p[0].text, save_pos)
	for dd in range(2):
		save_pos = save_data(data, sel_dd[dd].text, save_pos)
	for td in range(0, 36, 3):
		save_pos = save_data(data, sel_td[td+1].text, save_pos)
		save_pos = save_data(data, sel_td[td+2].text, save_pos)
	for td in range(36, 42, 2):
		save_pos = save_data(data, sel_td[td+1].text, save_pos)
	for dd in range(2, 29):
		if dd == 23:
			try:
				if sel_a[137]['href'][0:8] == '/en/data':
					text = ''
				else:
					text = sel_a[137]['href']
				save_pos = save_data(data, text, save_pos)
			except:
				save_pos = save_data(data, '', save_pos)
			continue
		save_pos = save_data(data, sel_dd[dd].text, save_pos)
	for td in range(42, 137, 5):
		Xpos = 0
		for findX in range(4):
			if sel_td[td+findX+1].text == 'X':
				Xpos = findX+1
				break
		save_pos = save_data(data, Xpos, save_pos)
	for dd in range(29, 85):
		if dd == 79:
			if sel_dd[dd].text.replace('\n','') == 'Financial Aid Web Site':
				text = ''
			else:
				text = sel_dd[dd].text
			save_pos = save_data(data, text, save_pos)
			continue
		if dd == 80:
			try:
				if sel_a[138]['href'][0:8] == '/en/data':
					text = ''
				else:
					text = sel_a[138]['href'].replace('\n', '').replace('Financial Aid Web Site', '')
				save_pos = save_data(data, text, save_pos)
			except:
				save_pos = save_data(data, '', save_pos)
			continue
		if dd == 81:
			try:
				if sel_a[dd+58]['href'][0:8] == '/en/data':
					text = ''
				else:
					text = sel_a[dd+58]['href']
				save_pos = save_data(data, text, save_pos)
			except:
				if sel_dd[dd].text.replace('\n', '') == 'Net Price Calculator URL':
					text = ''
				save_pos = save_data(data, text, save_pos)
			continue
		save_pos = save_data(data, sel_dd[dd].text, save_pos)
	text = ''
	for td in range(137, 150, 2):
		if sel_td[td].text == 'Baseball':
			save_pos = save_data(data, text, save_pos)
			break
		text += sel_td[td].text + ':'
		text += sel_td[td+1].text + ';'
	
	for dd in range(85, 130):
		save_pos = save_data(data, sel_dd[dd].text, save_pos)
	try:
		if sel_a[140]['href'][0:8] == '/en/data':
			text = ''
		else:
			text = sel_a[140]['href']
		save_pos = save_data(data, text, save_pos)
	except:
		save_pos = save_data(data, sel_dd[130].text, save_pos)
	save_pos = save_data(data, sel_ul[0].text.replace('\n', ';')[1::] + ',' + sel_ul[1].text.replace('\n', ';'), save_pos)
	for dd in range(131 ,157):
		save_pos = save_data(data, sel_dd[dd].text, save_pos)
	save_pos = save_data(data, sel_p[1].text, save_pos)
	save_pos = save_data(data, sel_ul[2].text.replace('\n', ';')[1::] + sel_ul[3].text.replace('\n', ';'), save_pos)
	save_pos = save_data(data, sel_p[2].text, save_pos)
	save_pos = save_data(data, sel_ul[4].text.replace('\n', ';')[1::], save_pos)
	for dd in range(157, 183):
		if dd == 162:
			try:
				if sel_a[141]['href'][0:8] == '/en/data':
					text = ''
				else:
					text = sel_a[141]['href']
				save_pos = save_data(data, text, save_pos)
				continue
			except:
				save_pos = save_data(data, sel_dd[dd].text, save_pos)
				continue
		save_pos = save_data(data, sel_dd[dd].text, save_pos)
	find_sport_form_beg_end = []
	for i in range(len(sel_tr)):
		if 'Offered' in sel_tr[i].text:
			find_sport_form_beg_end.append(i)	
	sport_women = ''
	sport_men = ''
	for i in range(find_sport_form_beg_end[0]+1, find_sport_form_beg_end[1]):
		sport_info = sel_tr[i].text.split('\n')
		sport_women += sport_info[1] + ':'
		sport_men += sport_info[1] + ':'
		pre = False
		if sport_info[2] == 'x':
			sport_women += 'Offered'
			pre = True
		if sport_info[3] == 'x':
			if pre == True:
				sport_women += ','
			sport_women += 'Scholarships'
		pre = False
		if sport_info[4] == 'x':
			sport_men += 'Offered'
			pre = True
		if sport_info[5] == 'x':
			if pre == True:
				sport_men += ','
			sport_men += 'Scholarships'
		sport_women += '; '
		sport_men += '; '
	save_pos = save_data(data, sport_women, save_pos)
	save_pos = save_data(data, sport_men, save_pos)
	for dd in range(183, 207):
		try:
			save_pos = save_data(data, sel_dd[dd].text, save_pos)
		except:
			pass
	csvWriter.writerow(data)

def main():
	data = ['']*311
	with requests.Session() as s:	
	# Get search page's html by cookies.
		# account_info = json.load(open('..//..//Account.json'))
		# Load my login info
		header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) ""AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
		logindata = {'LoginForm.LoginWithEmail': 'True', 'LoginForm.Username': 'jp6ru8958958@gmail.com', 'LoginForm.Email': 'jp6ru8958958@gmail.com', 'LoginForm.Password': 'cd958958', 'LoginForm.CanonicalUrl': '/en/explore-colleges/college-search/SearchByPreference/?SearchByPreference.SearchType=ByName&SearchByPreference.CollegeName=+', 'button': ''}
		p = s.post('https://www.collegedata.com/en/login/Submit/', headers=header, data=logindata)
		response = s.get('https://www.collegedata.com/en/explore-colleges/college-search/SearchByPreference/?SearchByPreference.SearchType=ByName&SearchByPreference.CollegeName=+')
	'''
	response = open('Soup_search_html.txt', 'r')
	'''
	soup = BeautifulSoup(response.text, 'html.parser')
	school_name_list = soup.select('div.t-title__details a') # School's name and Schoolinfo's link['href'] list.
	school_amount = int(len(school_name_list)/3)
	school_search_info_data = soup.select('td')[5::]
	# Write_result_as_file(school_name_list, 'Soup_search_school_name_list.txt')
	csvFile = open('cms_scrapy.csv', 'w', encoding='utf_8_sig')
	csvWriter = csv.writer(csvFile)
	# Csv file.
	set_field(csvWriter)
	# Set csv file's field.
	for school in range(school_amount): # school_amount
		print('(',school,'/',school_amount,')')
		save_pos = 0
		save_pos = save_data(data, school_name_list[school].text, save_pos)
		for vitals in range(2, 9):
			save_pos = save_data(data, school_search_info_data[(9 * school)+vitals].text.split('\n')[2], save_pos)
		for financial in range(2,7):
			save_pos = save_data(data, school_search_info_data[(8 * school) + financial + (9 * school_amount) + 1].text.split('\n')[2], save_pos)
		for students in range(1, 7):
			save_pos = save_data(data, school_search_info_data[(8 * school) + students + ((9 + 8) * school_amount) + 1].text.split('\n')[2], save_pos)
		set_data(csvWriter, school_name_list[school]['href'], data, save_pos)


if __name__ == '__main__':
	main()
