# YC Job Scraper

This project scrapes job openings from all hiring startups listed on [Y Combinator's Companies page](https://www.ycombinator.com/companies?isHiring=true). It combines **Selenium** (for handling infinite scrolling) and **Scrapy** (for fast structured data extraction), and supports **Zyte Smart Proxy Manager** for scalable, stealthy scraping.

**~3,000 jobs** have been scraped from **1,000+ companies** that are actively recruiting. You'll fin the csv file in the /yc_job/yc_jobs_all.csv or /yc_job/yc_jobs_all.csv file.

## Technologies
- Python  
- Scrapy  
- Selenium  
- Zyte
- dotenv  


## Features

- ✅ Scrapes all hiring YC startups using infinite scroll
- ✅ Extracts job titles, links, company names, salary, and location
- ✅ Uses Selenium for rendering JavaScript-heavy pages
- ✅ Uses Scrapy for fast and structured data parsing
- ✅ Supports Zyte Smart Proxy Manager integration
- ✅ Outputs data in formatted JSON & CSV files

## How to run
1. Clone the repository
```
git clone https://github.com/D1Asif/yc-jobs-scraper.git
cd yc-jobs-scraper
```
2. Create and activate a virtual environment
```
python -m venv venv
source venv/bin/activate 
```
3. Install dependencies
```
pip install -r requirements.txt
```
4. Create a .env file in the project root and add your Zyte API key (optional if using Zyte):
```
ZYTE_API_KEY=your_zyte_api_key
```
5. Go to the yc_jobs directory and run the spider
```
cd yc_jobs
scrapy crawl yc_job_spider -O all_yc_jobs.csv
```

## What's Coming Next

Here are some exciting features and improvements planned for future releases:

- 🔄 **Automated Scheduler**: Schedule the scraper to run daily or weekly using cron jobs or a task queue.
- 🌐 **Web Dashboard**: Simple UI to view job listings, filter by company/location, and download data.
- 📫 **Email Alerts**: Get notified when new YC job listings match your criteria.
- 🧠 **Job Matching AI**: Recommend jobs based on your resume or skillset using LLMs.
- ☁️ **Cloud Deployment**: Deploy to AWS/ZYTE.
