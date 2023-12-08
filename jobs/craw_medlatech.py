from core.crawlers.medlatech_crawler import MedlatecCrawler


def crawl_medlatech():
    crawler = MedlatecCrawler(is_multi_process=True)
    crawler.crawl([
        {
            "url": "https://medlatec.vn/chan-doan-hinh-anh",
            "num_pages": 79,
            "category": "Chẩn đoán hình ảnh"
        },
        {
            "url": "https://medlatec.vn/dinh-duong",
            "num_pages": 130,
            "category": "Dinh dưỡng"
        }
    ])