"""

"""

from core.crawlers.mediplus_crawler import MediplusCrawler


def crawl_mediplus():
    crawler = MediplusCrawler(is_multi_process=True)
    crawler.crawl([
        {
            "url": "https://www.mediplus.vn/kien-thuc-ve-benh/tieu-hoa",
            "num_pages": 10,
            "category": "Bệnh tiêu hóa"
        },
        {
            "url": "https://www.mediplus.vn/kien-thuc-ve-benh/co-xuong-khop",
            "num_pages": 7,
            "category": "Cơ – Xương – Khớp"
        },
        {
            "url": "https://www.mediplus.vn/kien-thuc-ve-benh/benh-xa-hoi",
            "num_pages": 4,
            "category": "Bệnh Xã Hội"
        },
        {
            "url": "https://www.mediplus.vn/kien-thuc-ve-benh/ho-hap",
            "num_pages": 1,
            "category": "Hô hấp"
        },
        {
            "url": "https://www.mediplus.vn/kien-thuc-ve-benh/nam-khoa",
            "num_pages": 8,
            "category": "Nam khoa"
        },
        {
            "url": "https://www.mediplus.vn/kien-thuc-ve-benh/nhi",
            "num_pages": 8,
            "category": "Nhi"
        },
        {
            "url": "https://www.mediplus.vn/kien-thuc-ve-benh/noi-than-kinh",
            "num_pages": 1,
            "category": "Nội thần kinh"
        },
        {
            "url": "https://www.mediplus.vn/kien-thuc-ve-benh/noi-ung-buou",
            "num_pages": 3,
            "category": "Nội ung bướu"
        },
        {
            "url": "https://www.mediplus.vn/kien-thuc-ve-benh/san-phu-khoa",
            "num_pages": 34,
            "category": "Sản phụ khoa"
        },
        {
            "url": "https://www.mediplus.vn/kien-thuc-ve-benh/tim-mach",
            "num_pages": 1,
            "category": "Tim mạch"
        },
        {
            "url": "https://www.mediplus.vn/kien-thuc-ve-benh/covid-19",
            "num_pages": 7,
            "category": "Covid-19"
        },
        {
            "url": "https://www.mediplus.vn/kien-thuc-ve-benh/da-lieu",
            "num_pages": 2,
            "category": "Da liễu"
        },
        {
            "url": "https://www.mediplus.vn/kien-thuc-ve-benh/xet-nghiem",
            "num_pages": 1,
            "category": "Xét nghiệm"
        },
        {
            "url": "https://www.mediplus.vn/kien-thuc-ve-benh/tham-do-chuc-nang",
            "num_pages": 11,
            "category": "Thăm dò chức năng"
        },
        {
            "url": "https://www.mediplus.vn/kien-thuc-ve-benh/tai-mui-hong",
            "num_pages": 1,
            "category": "Tai mũi họng"
        },
        {
            "url": "https://www.mediplus.vn/kien-thuc-ve-benh/ky-nang-so-cuu",
            "num_pages": 1,
            "category": "Kỹ năng sơ cứu"
        }
    ])