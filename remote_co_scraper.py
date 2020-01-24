import pandas as pd
from selenium import webdriver
from time import sleep
#import cookielib
import pdb
import http.cookiejar as cookielib
from selenium.webdriver.firefox.options import Options
import lxml
from bs4 import BeautifulSoup
import json
from lxml import html,etree
import glob

options = Options()
options.headless = True

print ('Launching Firefox..')
browser = webdriver.Firefox(options=options)
#print 'Entering to skidpaste.org...'
#browser.get('https://weworkremotely.com/remote-companies')
#print ('Waiting 15 seconds...')

#/html/body/main/div[2]/div/div[1]/div[4]/div/div[2]/div/a[1]/div
#/html/body/main/div[2]/div/div[1]/div[4]/div/div[2]/div/a[9]/div

print("First request")

for i in range(1,2):
	names=[]
	des=[]
	webs=[]
	browser.get("https://remote.co/remote-jobs/it/")
	#pdb.set_trace()
	#pre = browser.find_ele  ment_by_name("json").text
	#data = json.loads(pre)
	#print(data)
	html_source = browser.page_source
	#print(html_source)
	tree = html.fromstring(html_source)
	#json_obj = json.loads(tree.xpath('//div[@id="json"]/text()')[0])
	companies = tree.xpath('/html/body/main/div/div/div/div/div/div/div/a/div/div/div/div/p/text()')
	real_companies=[]
	for company in companies:
		company = company.replace("|","")
		company = company.replace("\\n","")
		company = company.replace("\\t","")
		company = company.replace(" ","")
		#print(company)
		if(len(company.strip())>0):
			company=company.strip()
			#company = company.encode('utf-8')
			company = company.split("\\")[0]
			real_companies.append(company)	
	#print(real_companies)
	#print(len(real_companies))


	titles = tree.xpath('/html/body/main/div/div/div/div/div/div/div/a/div/div/div/div/p/span/text()')
	real_titles=[]
	for title in titles:
		title = title.replace("|","")
		title = title.replace("\\n","")
		title = title.replace("\\t","")
		title = title.replace("  ","")
		if(len(title.strip())>0):
			real_titles.append(title)
	#print(real_titles)
	#print(len(real_titles))	


	dates = tree.xpath('/html/body/main/div/div/div/div/div/div/div/a/div/div/div/div/p/span/small/date/text()')
	real_dates=[]
	for date in dates:
		date = date.replace("|","")
		date = date.replace("\\n","")
		date = date.replace("\\t","")
		date = date.replace("  ","")
		if(len(date.strip())>0):
			real_dates.append(date)
	#print(real_dates)
	print(len(real_dates))	
	
	links = tree.xpath('/html/body/main/div/div/div/div[4]/div/div/div/a/@href')
	if(len(links)==0):
		links = tree.xpath('/html/body/main/div/div/div/div[5]/div/div/div/a/@href')
	print(len(links))

	#Description
	#/html/body/main/div/div/div[1]/div[2]/div/div[1]/div[3]

	dess=[]
	a_links=[]

	for i in range(0,len(links)):
		try:
			browser.get("https://remote.co"+links[i])
			html_source = browser.page_source
			#print(html_source)
			tree = html.fromstring(html_source)
			try:
				a_link = tree.xpath('/html/body/main/div/div/div[1]/div[2]/div/div[1]/div[4]/a/@href')[0]
				#print(a_link)
				a_links.append(a_link)
			except :
				a_links.append(" ")
			#json_obj = json.loads(tree.xpath('//div[@id="json"]/text()')[0])
			des = tree.xpath('/html/body/main/div/div/div[1]/div[2]/div/div[1]/div[3]')[0]
			des = str(etree.tostring(des))
			des = BeautifulSoup(des, "lxml").text
			des = des.replace("\\n","")
			des = des.replace("\\t","")
			#des =des.encode('utf-8').strip()
			#des.des.replace("","")
			des=des[2:-1]
			dess.append(des)
		except:
			dess.append(" ")
		sleep(1)
		#print(i)
	print(len(dess))
	df = pd.DataFrame({"Title":real_titles,"Description":dess,"RC_Link":links,"posted_date":real_dates,"Companies":real_companies,"Apply_link":a_links})
	df.to_csv("RC_Jobs.csv",index=False)
	add=[]
	web=[]
	name=[]
	num=[]

browser.stop_client()
browser.close()
