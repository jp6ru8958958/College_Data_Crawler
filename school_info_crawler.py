import requests
from bs4 import BeautifulSoup

def put_data(field, data, pos, a, b):
	field[pos] = a
	data[pos] = b

def main():
	
	url = 'https://www.collegedata.com/college/West-Texas-A-M-University/?tab=profile-admission-tab'
	fr = requests.get(url)
	'''
	fr = open('school_info.txt', 'r')
	'''
	soup = BeautifulSoup(fr.text, 'html.parser')

	overview_intro = soup.select('p.h6.mb-4')
	overview_intro_webLink = soup.select('p.h6 a')
	sel_p = soup.find_all('p')[64::]
	sel_field = soup.find_all('dt')
	sel_data = soup.find_all('dd')
	sel_td = soup.find_all('td')
	sel_span = soup.find_all('span')
	sel_sex_prop = soup.select('div b')
	sel_link = soup.select('a')
	sel_ul = soup.select('ul.list--nice')
	field_info = ['']*350
	school_info = ['']*350
	sel_statbar = soup.find('div', class_='statbar__item')[1].div.text
	
	put_data(field_info, school_info, 20, 'introduction', overview_intro[0].text.replace('\n', ''))
	put_data(field_info, school_info, 21, 'website', overview_intro_webLink[0]['href'])
	put_data(field_info, school_info, 24, sel_span[41].text, sel_span[40].text)
	put_data(field_info, school_info, 25, 'Women', sel_sex_prop[0].text + sel_span[42].text.replace(' Women', ''))
	put_data(field_info, school_info, 26, 'Men', sel_sex_prop[1].text + sel_span[43].text.replace(' Men', ''))
	put_data(field_info, school_info, 27, sel_span[45].text.replace('\n', ''), sel_span[44].text.replace('\n', ''))
	put_data(field_info, school_info, 28, 'Entrance Difficulty', sel_p[0].text)
	set_pos=29
	for i in range(300):
		if set_pos == 29:
			title = '(High School Preparation)'
			for i in range(33, 35):
				put_data(field_info, school_info, set_pos, title+sel_field[i].text, sel_data[i].text)
				set_pos+=1
		elif set_pos == 31:
			title = '(High School Units Required or Recommended)('
			for i in range(5, 26, 3):
				put_data(field_info, school_info, set_pos, title+sel_td[i].text+')Required Units', sel_td[i+1].text)
				set_pos+=1
				put_data(field_info, school_info, set_pos, title+sel_td[i].text+')Recommended Units', sel_td[i+2].text)
				set_pos+=1
		elif set_pos == 45:
			title = '(Examinations)'
			for i in range(26, 41, 3):
				put_data(field_info, school_info, set_pos, title + '(' + sel_td[i].text+')Required Units', sel_td[i+1].text)
				set_pos+=1
				put_data(field_info, school_info, set_pos, title + '(' + sel_td[i].text+')Scores Due in Admissions Office', sel_td[i+2].text)
				set_pos+=1
		elif set_pos == 55:
			title = '(Examinations)'
			for i in range(41, 47,2):
				put_data(field_info, school_info, set_pos, title + sel_td[i].text, sel_td[i+1].text)
				set_pos+=1
		elif set_pos == 58:
			title = '(Admissions Office)'
			for i in range(35, 40):
				put_data(field_info, school_info, set_pos, title + sel_field[i].text, sel_data[i].text)
				set_pos+=1
		elif set_pos == 63:
			title = '(Application Dates and Fees)'
			for i in range(40, 48):
				put_data(field_info, school_info, set_pos, title + sel_field[i].text, sel_data[i].text)
				set_pos+=1
		elif set_pos == 71:
			title = '(Early Admission)'
			for i in range(48, 54):
				put_data(field_info, school_info, set_pos, title + sel_field[i].text, sel_data[i].text)
				set_pos+=1
		elif set_pos == 77:
			title = '(Application Form)'
			for i in range(54, 56):
				put_data(field_info, school_info, set_pos, title + sel_field[i].text, sel_data[i].text)
				set_pos+=1
			put_data(field_info, school_info, set_pos, title + sel_field[i].text, sel_link[137]['href'])
			set_pos+=1
		elif set_pos == 80:
			title = '(Other Application Requirements)'
			for i in range(57, 62):
				put_data(field_info, school_info, set_pos, title + sel_field[i].text, sel_data[i].text)
				set_pos+=1
		elif set_pos == 85:
			title = '(Selection of Students)'
			for i in range(47, 142, 5):
				for find_X in range(5):
					num=0
					if sel_td[i+find_X].text == 'X': 
						num = find_X
						break
				put_data(field_info, school_info, set_pos, title + sel_td[i].text, num)
				set_pos+=1
		elif set_pos == 104:		
			title = '(Profile of Fall Admission)'
			for i in range(62, 68, 3):
				put_data(field_info, school_info, set_pos, title + sel_field[i].text, sel_data[i].text)
				set_pos+=1
				put_data(field_info, school_info, set_pos, title + '(' + sel_field[i].text + ')' + sel_field[i+1].text, sel_data[i+1].text)
				set_pos+=1
				put_data(field_info, school_info, set_pos, title + '(' + sel_field[i].text + ')' + sel_field[i+2].text, sel_data[i+2].text)
				set_pos+=1
			for i in range(68, 73):
				put_data(field_info, school_info, set_pos, title + sel_field[i].text, sel_data[i].text)
				set_pos+=1
		elif set_pos == 115:
			title = '(Grade Point Average of Enrolled Freshmen (4.0 scale))'
			put_data(field_info, school_info, set_pos, title + sel_field[73].text, sel_data[73].text)
			set_pos+=1	
			for i in range(74, 80):
				put_data(field_info, school_info, set_pos, title + '(' + sel_field[73].text + ')' + sel_field[i].text, sel_data[i].text)
				set_pos+=1
		elif set_pos == 122:
			title = '(SAT Scores of Enrolled Freshmen)'
			for i in range(80, 94, 7):
					put_data(field_info, school_info, set_pos, title + sel_field[i].text , sel_data[i].text)
					set_pos+=1
					for y in range(1, 7):
						put_data(field_info, school_info, set_pos, title + '(' + sel_field[i].text + ')' +sel_field[i+y].text, sel_data[i+y].text)
						set_pos+=1
		
		elif set_pos == 136:
			title = '(ACT Scores of Enrolled Freshmen)'
			put_data(field_info, school_info, set_pos, title + sel_field[80].text, sel_data[80].text)
			set_pos+=1	
			for i in range(94, 101):
				put_data(field_info, school_info, set_pos, title + '(' + sel_field[80].text + ')' + sel_field[i].text, sel_data[i].text)
				set_pos+=1
		elif set_pos == 144:
			title = '(Other Qualifications of Enrolled Freshmen)'
			for i in range(101, 106):
				put_data(field_info, school_info, set_pos, title + sel_field[i].text, sel_data[i].text)
				set_pos+=1
		elif set_pos == 149:
			title = '(Tuition and Expenses)'
			put_data(field_info, school_info, set_pos, title + sel_field[107].text, sel_data[107].text)
			set_pos+=1	
			for i in range(108, 111):
				put_data(field_info, school_info, set_pos, title + '(' + sel_field[107].text + ')' + sel_field[i].text, sel_data[i].text)
				set_pos+=1
			put_data(field_info, school_info, set_pos, title + sel_field[111].text, sel_data[111].text)
			set_pos+=1
		elif set_pos == 154:
			title = '(Applying for Financial Aid)'
			title2 = '(Financial Aid Office)'
			put_data(field_info, school_info, set_pos, title + title2 + sel_field[112].text, sel_data[112].text)
			set_pos+=1
			try:
				put_data(field_info, school_info, set_pos, title + title2 + sel_field[113].text, sel_link[138]['href'])
				set_pos+=1
			except:
				put_data(field_info, school_info, set_pos, title + title2 + sel_field[113].text, '')
				set_pos+=1
			
			try:
				put_data(field_info, school_info, set_pos, title + title2 + sel_field[114].text, sel_link[139]['href'])
				set_pos+=1
			except:
				put_data(field_info, school_info, set_pos, title + title2 + sel_field[114].text, '')
				set_pos+=1
			title2 = '(Application Process)'
			for i in range(140, 143):
				put_data(field_info, school_info, set_pos, title + title2 + sel_field[i].text, sel_data[i].text)
				set_pos+=1
			put_data(field_info, school_info, set_pos, title + '(Forms Required)' + sel_td[142].text, sel_td[143].text)
			set_pos+=1	
		elif set_pos == 161:
			title = '(Profile of 2018 - 19 Financial Aid)'
			title2 = '(Freshman)'
			for i in range(118, 128):
				if(124<=i and i<127):
					put_data(field_info, school_info, set_pos, title + title2 + '(' + sel_field[123].text + ')'+sel_field[i].text, sel_data[i].text)
					set_pos+=1
				else:
					put_data(field_info, school_info, set_pos, title + title2 + sel_field[i].text, sel_data[i].text)
					set_pos+=1
			title2 = '(All Undergraduates)'
			for i in range(128, 138):
				if(134<=i and i<136):
					put_data(field_info, school_info, set_pos, title + title2 + '(' + sel_field[133].text + ')'+sel_field[i].text, sel_data[i].text)
					set_pos+=1
				else:
					put_data(field_info, school_info, set_pos, title + title2 + sel_field[i].text, sel_data[i].text)
					set_pos+=1
			title2 = '(Borrowing)'
			for i in range(138, 142):
				if(140==i or i==141):
					put_data(field_info, school_info, set_pos, title + title2 + '(' + sel_field[139].text + ')'+sel_field[i].text, sel_data[i].text)
					set_pos+=1
				else:
					put_data(field_info, school_info, set_pos, title + title2 + sel_field[i].text, sel_data[i].text)
					set_pos+=1
		elif set_pos == 185:
			title = '(Financial Aid Programs)'
			title2 = '(Loans)'
			for i in range(142, 147):
				if i == 145: title2 = '(Scholarships and Grants)'
				put_data(field_info, school_info, set_pos, title + title2 + sel_field[i].text, sel_data[i].text)
				set_pos+=1
			title2 = '(Non-Need Awards)'
			for i in range(147, 159, 3):
				put_data(field_info, school_info, set_pos, title + title2 + sel_field[i].text, sel_data[i].text)
				set_pos+=1
				put_data(field_info, school_info, set_pos, title + title2 + '(' + sel_field[i].text + ')' + sel_field[i+1].text, sel_data[i+1].text)
				set_pos+=1
				put_data(field_info, school_info, set_pos, title + title2 + '(' + sel_field[i].text + ')' + sel_field[i+2].text, sel_data[i+2].text)
				set_pos+=1
			title2 = '(Employment)'
			for i in range(159, 161):
				put_data(field_info, school_info, set_pos, title + title2 + sel_field[i].text, sel_data[i].text)
				set_pos+=1
		elif set_pos == 204:
			for i in range(161, 164):
				if i == 163:
					try:
						put_data(field_info, school_info, set_pos, sel_field[i].text, sel_link[140]['href'])
						set_pos+=1
						continue
					except:
						put_data(field_info, school_info, set_pos, sel_field[i].text, '')
						set_pos+=1
						continue
						
				put_data(field_info, school_info, set_pos, sel_field[i].text, sel_data[i].text)
				set_pos+=1
		elif set_pos == 207:
			title = '(Undergraduate Education)'
			title2 = 'Undergraduate Majors'
			put_data(field_info, school_info, set_pos, title + '(' + title2 + ')', sel_ul[0].text.replace('\n', ';')[1::] + ',' + sel_ul[1].text.replace('\n', ';'))
			set_pos+=1
			for i in range(164, 169):
				put_data(field_info, school_info, set_pos, title + '(' + title2 + ')' + sel_field[i].text, sel_data[i].text)
				set_pos+=1
		elif set_pos == 213:
			title = '(Curriculum and Graduation Requirements)'
			for i in range(169, 173):
				put_data(field_info, school_info, set_pos, title + sel_field[i].text, sel_data[i].text)
				set_pos+=1
		elif set_pos == 217:
			title = '(Faculty and Instruction)'
			for i in range(173, 178):
				put_data(field_info, school_info, set_pos, title + sel_field[i].text, sel_data[i].text)
				set_pos+=1
		elif set_pos == 222:
			title = '(Advanced Placement)'
			for i in range(178, 181):
				put_data(field_info, school_info, set_pos, title + sel_field[i].text, sel_data[i].text)
				set_pos+=1
		elif set_pos == 225:
			title = '(Academic Resources)'
			for i in range(181, 186):
				put_data(field_info, school_info, set_pos, title + sel_field[i].text, sel_data[i].text)
				set_pos+=1
		elif set_pos == 230:
			title = '(Academic Support Services)'
			for i in range(186, 190):
				put_data(field_info, school_info, set_pos, title + sel_field[i].text, sel_data[i].text)
				set_pos+=1
		elif set_pos == 234:
			title = '(Graduate/Professional School Education)'
			put_data(field_info, school_info, set_pos, 'Master\'s Degrees Offered', sel_p[1].text)
			set_pos+=1
			put_data(field_info, school_info, set_pos, title + 'Master\'s Programs of Study', sel_ul[2].text.replace('\n' , ';')[1::] + sel_ul[3].text.replace('\n', ';'))
			set_pos+=1
			put_data(field_info, school_info, set_pos, title + 'Doctoral Degrees Offered ', sel_p[2].text)
			set_pos+=1
			put_data(field_info, school_info, set_pos, title + 'Doctoral Programs of Study', sel_ul[4].text.replace('\n' , ';')[1::])
			set_pos+=1
		elif set_pos == 238:
			title = '(Location and Setting)'
			for i in range(190, 198):
				if i == 190:
					title2 = ''
				elif i == 193:
					title2 = '(Weather)'
				elif i == 195:
					title2 = '(Getting Around)'
				if set_pos == 242:
					put_data(field_info, school_info, set_pos, title + sel_field[i].text, sel_link[141]['href'])
					set_pos+=1
					continue
				put_data(field_info, school_info, set_pos, title + title2 + sel_field[i].text, sel_data[i].text)
				set_pos+=1
		elif set_pos == 246:
			title = '(Housing)'
			title2 = ''
			for i in range(198, 213):
				if i == 205:
					title = '(Security)'
				elif i == 210:
					title = '(Personal Support Services)'
				put_data(field_info, school_info, set_pos, title + sel_field[i].text, sel_data[i].text)
				set_pos+=1
		elif set_pos == 261:
			title = '(Sports and Recreation)'
			title2 = '(Intercollegiate Athletics)'
			for i in range(213, 216):
				put_data(field_info, school_info, set_pos, title + title2 + sel_field[i].text, sel_data[i].text)
				set_pos+=1
			title2 = '(Intercollegiate Sports Offered)'
			sex = 'Women'
			start = 199
			for scan in range(190, 260):
				if sel_td[scan].text == 'Baseball':
					start = scan
					break
			for i in range(start, start+66, 3):
				if i==start+30: sex = 'Men'
				if sel_td[i+1].text == 'x': 
					text1 = 'Offered;'
				else:
					text1 = ''
				if sel_td[i+2].text == 'x':
					text2 = 'Scholarships;'
				else:
					text2 = ''
				put_data(field_info, school_info, set_pos, title + title2 + '(' + sex + ')' + sel_td[i].text, text1 + text2)
				set_pos+=1
			for i in range(216, 218):
				put_data(field_info, school_info, set_pos, title + title2 + sel_field[i].text, sel_data[i].text)
				set_pos+=1
			title2 = '(Recreational Sports)'
			put_data(field_info, school_info, set_pos, title + title2 + sel_field[218].text, sel_data[218].text)
			set_pos+=1
		elif set_pos == 289:
			title = '(Student Activities)'
			for i in range(219, 223):
				put_data(field_info, school_info, set_pos, title + sel_field[i].text, sel_data[i].text)
				set_pos+=1
		elif set_pos == 293:
			title = '(Student Body)'
			for i in range(223, 232):
				if i == 225 or i == 226:
					put_data(field_info, school_info, set_pos, title + '(' + sel_field[224].text + ')' + sel_field[i].text, sel_data[i].text)
					set_pos+=1
					continue
				put_data(field_info, school_info, set_pos, title + sel_field[i].text, sel_data[i].text)
				set_pos+=1
		elif set_pos == 302:
			title = '(Undergraduate Retention and Graduation)'
			for i in range(232, 236):
				put_data(field_info, school_info, set_pos, title + sel_field[i].text, sel_data[i].text)
				set_pos+=1
		elif set_pos == 306:
			title = '(After Graduation)'
			for i in range(236, 240):
				if i == 237:
					put_data(field_info, school_info, set_pos, title + '(' + sel_field[i-1].text + ')' + sel_field[i].text, sel_data[i].text)
					set_pos+=1
					continue
				put_data(field_info, school_info, set_pos, title + title2 + sel_field[i].text, sel_data[i].text)
				set_pos+=1
			
			
			

		
	
		
	
	



						



	for pt in range(len(field_info)):
		print(pt)
		print(field_info[pt])
		print(school_info[pt], '\n')
	'''
	for i in range(len(sel_p)):
		print(i)
		print(sel_p[i].text)
'''	
	print(sel_statbar)
	
if __name__ == '__main__':
	main()
