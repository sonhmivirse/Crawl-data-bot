

from core.crawlers.vietduc_crawler import VietducCrawler

def crawl_vietduc():
    crawler = VietducCrawler(is_multi_process=True)
    crawler.crawl([
       {
            "url": "https://benhvienvietduc.org/chuyen-muc/tin-y-hoc",
            "num_pages": 42,
            "catgory": "Tin tức y học"
       }
    ])