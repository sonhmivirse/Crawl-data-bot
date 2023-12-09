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

class TamAnhCrawler(TextCrawler):
    def __init__(self, is_multi_process=False, max_workers=8):
        self.db = self.connect_db()
        self.is_multi_process = is_multi_process
        self.max_workers = max_workers
                
    def crawl_url(self, source, summary="", title="", category=""):
        """Crawl from an url"""
        coll_name = "medical_tamanh"
        try: 
            collection = self.db[coll_name]
            exist_data = collection.find({"url": source})
            if len(list(exist_data)):
                print(f"Exist crawl data from url {source}")
                return
            
            res = requests.get(source, headers=usr_agent)
            html = res.content
            soup = BeautifulSoup(html, 'html.parser')
            
            title = soup.select_one("div.post_info div.title h1")
            title = title.get_text(strip=True) if title else ""
                        
            text = soup.select_one("div#ftwp-postcontent")
            
            if text:
                for unwanted_id in ["ftwp-container-outer", "gioi-thieu-dich-vu-bvdk-tam-anh"]:
                    for element in text.select(f"div#{unwanted_id}"):
                        if element:
                            element.decompose()
                for unwanted_class in ["alert-info"]:
                    for element in text.select(f"div.{unwanted_class}"):
                        if element:
                            element.decompose()
            
            text = str(text) if text else ""
            
            saved_obj = {
                "text": text,
                "title": title,
                "summary": summary,
                "category": category,
                "source": "Tâm Anh",
                "url": source
            }
                
            collection.insert_one(saved_obj)
        except Exception as e:
            print("ERROR extract disease: ", str(e))
            with open("error_tamanh.txt", "a") as f:
                f.write(f"\n{source}")
            
    
    def crawl_source(self, source):
        """Crawl from a parent list source (include pages)"""
        root_url = "https://tamanhhospital.vn/"
        query_url = "https://tamanhhospital.vn/wp-content/themes/wg/ajax_news.php"
        num_page = source.get("num_pages")
        url = source.get("url")
        category = source.get("category")
        if num_page > 1:
            idpost = source.get("idpost")
        headers = {
            'authority': 'tamanhhospital.vn',
            'accept': 'text/html, */*; q=0.01',
            'accept-language': 'vi,vi-VN;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'cookie': '_gcl_au=1.1.657725870.1701584803; _fbp=fb.1.1701584804027.603647362; __admUTMtime=1701584808; __RC=4; dtdz=6bd478b1-bc7c-4c93-bc03-1ea6c5376e8e; __iid=; __iid=; __su=0; __su=0; _ym_uid=1672997064364465324; _ym_d=1701584810; __R=1; __tb=0; _gid=GA1.2.1610292552.1702117952; _ym_isad=2; _ym_visorc=b; __IP=20418118; _gat_UA-83362508-1=1; __uif=__uid%3A346731728320383403%7C__ui%3A2%252C4%7C__create%3A1667317283; _ga_2EKFK803DM=GS1.1.1702121187.3.1.1702122855.58.0.0; _ga_G9P9P58D5Y=GS1.1.1702121187.3.1.1702122855.58.0.0; _ga=GA1.2.669364468.1701584803',
            'origin': 'https://tamanhhospital.vn',
            'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }
        
        headers["referer"] = url
        
        print(f"Start crawling from  {url}...")
        start_page = 1
        
        for page in tqdm(range(start_page, num_page + 1), desc="Crawl page", unit="page"):
            try:
                if num_page > 1:
                    data = {
                        'cur_trang': str(page),
                        'idpost': idpost,
                        'cur_limit': '12',
                    }
                    page_html = requests.post(query_url, headers=headers, data=data)
                else:
                    page_html = requests.get(url, headers=usr_agent)
                page_html = page_html.content
                
                soup = BeautifulSoup(page_html, 'html.parser')

                list_items = soup.select("div.item_post div.info_chuyengia>a")
                for item in list_items:
                    crawl_url = item.get("href")
                    self.crawl_url(crawl_url, category=category)
                time.sleep(1)
            except Exception as e:
                print(f"\nError crawl source - {source}- page: {page}: {str(e)}")     
                with open("Error_page_tamanh.txt", "a") as f:
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