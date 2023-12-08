from jobs.craw_medlatech import crawl_medlatech
from jobs.crawl_mediplus import crawl_mediplus
from jobs.crawl_thucuc import crawl_thucuc
from jobs.craw_vietduc import crawl_vietduc

if __name__ == "__main__":
    # crawl_medlatech()
    
    crawl_mediplus()
    crawl_thucuc()
    crawl_vietduc()