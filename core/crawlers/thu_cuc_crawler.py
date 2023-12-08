from utils.base_crawl import TextCrawler, usr_agent

import os
from bs4 import BeautifulSoup
import requests
import time
from tqdm import tqdm 
from pymongo import MongoClient
from dotenv import load_dotenv
import concurrent.futures
import json

load_dotenv()

class ThucucCrawler(TextCrawler):
    def __init__(self, is_multi_process=False, max_workers=8):
        self.db = self.connect_db()
        self.is_multi_process = is_multi_process
        self.max_workers = max_workers
                
    def crawl_url(self, source, summary="", title="", category=""):
        """Crawl from an url"""
        coll_name = "medical_thucuc"
        try: 
            collection = self.db[coll_name]
            exist_data = collection.find({"url": source})
            if len(list(exist_data)):
                print(f"Exist crawl data from url {source}")
                return
            
            res = requests.get(source, headers=usr_agent)
            html = res.content
            soup = BeautifulSoup(html, 'html.parser')
            
            title = soup.select_one("div#primary article h1.entry-title__h1")
            title = title.get_text(strip=True) if title else ""
                        
            text = soup.select_one("div#primary article div.entry-content")
            
            if text:
                for unwanted_id in ["ez-toc-container"]:
                    for element in text.select(f"div#{unwanted_id}"):
                        element.decompose()
            
            text = str(text) if text else ""
            
            saved_obj = {
                "text": text,
                "title": title,
                "summary": summary,
                "category": category,
                "source": "Thu cúc",
                "url": source
            }
                
            collection.insert_one(saved_obj)
        except Exception as e:
            print("ERROR extract disease: ", str(e))
            with open("error_thucuc.txt", "a") as f:
                f.write(f"\n{source}")
            
    
    def crawl_source(self, source):
        """Crawl from a parent list source (include pages)"""
        root_url = "https://benhvienthucuc.vn"
        num_page = source.get("num_pages")
        url = source.get("url")
        category = source.get("category")
        print(f"Start crawling from  {url}...")
        start_page = 1
        
        for page in tqdm(range(start_page, num_page + 1), desc="Crawl page", unit="page"):
            try:
                url_with_page = f"{url}/page/{page}"
                page_html = requests.get(url_with_page, headers=usr_agent)
                page_html = page_html.content
                
                soup = BeautifulSoup(page_html, 'html.parser')
                # Find the ul tag inside the post_list_div
                list_items = soup.select("div.entry-loop li a")
                for item in list_items:
                    crawl_url = item.get("href")
                    self.crawl_url(crawl_url, category=category)
                time.sleep(1)
            except Exception as e:
                print(f"\nError crawl source - {source}- page: {page}: {str(e)}")     
                with open("Error_page_thucuc.txt", "a") as f:
                    f.write(f"\n{source.get('url')}?page={page}") 
        
    def crawl_one_cpu(self, sources=[]):
        """Crawl with one process"""
    
    def crawl_mp(self, sources=[]):
        """Crawl with multiprocessing"""
        try:
            with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                executor.map(self.crawl_source, sources)
        except Exception as e:
            print("Error crawl data - ", str(e))
    
    def crawl(self, sources=[]):
        """Crawl method"""
        if self.is_multi_process:
            self.crawl_mp(sources)
        else:
            self.crawl_one_cpu(sources)            
    def craw_scheduler(self):
        """Crawl scheduler"""