# YC Job Scraper

This project scrapes job openings from all hiring startups listed on [Y Combinator's Companies page](https://www.ycombinator.com/companies?isHiring=true). It combines **Selenium** (for handling infinite scrolling) and **Scrapy** (for structured data extraction), and supports **Zyte Smart Proxy Manager** for scalable, stealthy scraping.

~3,000 jobs have been scraped from 1,000+ companies that are actively recruiting. You'll fin the csv file in the /yc_job/yc_jobs_all.csv or /yc_job/yc_jobs_all.csv file.

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
