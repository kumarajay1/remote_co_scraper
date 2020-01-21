import pandas as pd
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import time
from datetime import datetime

ap = PlainTextAuthProvider(username="ubuntu", password="bar")
df = pd.read_csv('./RC_Jobs.csv')
print(df.columns)

cluster = Cluster(['52.66.237.254'], auth_provider=ap)
session = cluster.connect('jobs_data')
query = "INSERT INTO remote_jobs(apply_link,company_name,job_link,description,job_title,job_type,location,posted_date,remote,salary,scraped_date,scraped_from) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)"
prepared = session.prepare(query)

start_time = time.time()
print("started")

for index, row in df.iterrows():
	#print(row)
	session.execute(prepared, (str(row.Apply_link),str(row.Companies),str(row.RC_Link),str(row.Description),str(row.Title),str("Remote"),str(" "),str(row.posted_date),True,"Not Mentioned",datetime.now(),"Remote_Co"))
print("--- %s seconds ---" % (time.time() - start_time))
