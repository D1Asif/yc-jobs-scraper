import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from scrapy.http import HtmlResponse
import json

class YcSpider(scrapy.Spider):
    name = "yc_job_spider"

    def start_requests(self):
        options = Options()
        # options.add_argument("--headless")  # Run in headless mode
        driver = webdriver.Chrome(options=options)

        try:
            # Open the Y Combinator companies page with specified filters
            url = "https://www.ycombinator.com/companies?isHiring=true"
            driver.get(url)

            # Allow the page to load
            time.sleep(3)

            # Get initial scroll height
            last_height = driver.execute_script("return document.body.scrollHeight")

            while True:
                # Scroll down to the bottom
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                # Wait for new content to load
                time.sleep(3)

                # Calculate new scroll height and compare with last scroll height
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    # If heights are the same, all content is loaded
                    break
                last_height = new_height

            # After all companies are loaded, extract their href links
            company_elements = driver.find_elements(By.CSS_SELECTOR, "a._company_i9oky_355")  # Update selector as needed
            company_links = [elem.get_attribute("href") for elem in company_elements]

            with open("hiring_company_links_all.json", "w") as f:
                json.dump(company_links, f, indent=4)

            # Output the list of company hrefs
            for link in company_links:
                jobs_link = link.rstrip("/") + "/jobs"  # Ensures single slash
                yield scrapy.Request(jobs_link)
        finally:
            # Close the browser
            driver.quit()

    def parse(self, response):
        jobs = response.css(".divide-y > div")

        for job in jobs:
            yield {
                "title": job.css(".ycdc-with-link-color > a ::text").get(),
                "link": response.urljoin(job.css(".ycdc-with-link-color > a ::attr(href)").get()),
                "company": response.url.strip("/").split("/")[-2].replace("-", " ").title(),
                "salary": job.css(".ycdc-with-link-color + div :nth-child(2) ::text").get(),
                "location": job.css(".ycdc-with-link-color + div :nth-child(1) ::text").get()
            }
