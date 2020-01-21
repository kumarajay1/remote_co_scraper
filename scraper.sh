export PATH=$PATH:/home/ubuntu/angle_co_scrape
echo "scraper starting"
python3 ./remote_co_scraper/remote_co_scraper.py 
sleep 3 
echo "Scraped the job details"
python3 ./remote_co_scraper/insert_into_db.py
echo "Inserted into DB"
rm -rf remote_co_scraper
