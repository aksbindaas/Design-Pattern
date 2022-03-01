from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import pandas as pd
import redis
import dateparser

r = redis.Redis(
    host='localhost',
    port=6379)


driver = webdriver.Chrome('/usr/local/bin/chromedriver')
for page_number in range(1, 11):
	URL = "https://www.naukri.com/python-jobs-"+str(page_number)
	driver.get(URL);
	delay = 3  # seconds
	try:
	    myElem = WebDriverWait(driver, delay).until(
	        EC.presence_of_element_located((By.CLASS_NAME, 'pagination mt-64 mb-60')))
	    print("Page is ready!")
	except TimeoutException:
	    print("Loading took too much time!")

	soup = BeautifulSoup(driver.page_source, 'html5lib')

	df = pd.DataFrame(columns=['Title', 'Company', 'Experience',
	                  'Salary', 'Location', 'Job_Post_History'])

	results = soup.find(class_='list')

	job_elems = results.find_all('article', class_='jobTuple bgWhite br4 mb-8')

	for job_elem in job_elems:
	        # Post Title
	        Title = job_elem.find('a', class_='title fw500 ellipsis')

	        # Company Name
	        Company = job_elem.find('a', class_='subTitle ellipsis fleft')

	        # Years of experience Required
	        Exp = job_elem.find(
	            'li', class_='fleft grey-text br2 placeHolderLi experience')
	        if Exp != None:
	        	Exp_span = Exp.find('span', class_='ellipsis fleft fs12 lh16')
		        if Exp_span is None:
		            continue
		        else:
		            Experience = Exp_span.text

	        # Salary offered for the job
	        Sal = job_elem.find(
	            'li', class_='fleft grey-text br2 placeHolderLi salary')
	        Sal_span = Sal.find('span', class_='ellipsis fleft fs12 lh16')
	        if Sal_span is None:
	            continue
	        else:
	            Salary = Sal_span.text

	        # Location for the job post
	        Loc = job_elem.find(
	            'li', class_='fleft grey-text br2 placeHolderLi location')
	        Loc_exp = Loc.find('span', class_='ellipsis fleft fs12 lh16')
	        if Loc_exp is None:
	            continue
	        else:
	            Location = Loc_exp.text

	        # Number of days since job posted
	        Hist = job_elem.find(
	            "div", ["type br2 fleft grey", "type br2 fleft green"])
	        Post_Hist = Hist.find('span', class_='fleft fw500')
	        if Post_Hist is None:
	            continue
	        else:
                 fewHours = "Few Hours Ago"
                 if fewHours.upper() == Post_Hist.text.upper():
                    Post_History = dateparser.parse("1 Hours Ago").strftime("%Y-%m-%d")
                 else:
                    Post_History = dateparser.parse(Post_Hist.text).strftime("%Y-%m-%d")

	        df=df.append({'Title':Title.text,'Company':Company.text,'Experience':Experience,'Salary':Salary,'Location':Location,'Job_Post_History':Post_History},ignore_index = True)
	        r.set(r'page-'+str(page_number),df.to_json (orient='records'))
