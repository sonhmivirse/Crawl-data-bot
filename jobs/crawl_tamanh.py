
from core.crawlers.tamanh_crawler import TamAnhCrawler

def crawl_tamanh():
    crawler = TamAnhCrawler(is_multi_process=True)
    crawler.crawl([
        {
            "url": "https://tamanhhospital.vn/chuyen-khoa/trung-tam-ho-tro-sinh-san-ivfta/",
            "category": "Hỗ trợ sinh sản",
            "num_pages": 21,
            "idpost": "13243"
        },
        {
            "url": "https://tamanhhospital.vn/chuyen-khoa/khoa-ngoai-vu/",
            "category": "Ngoại vú",
            "num_pages": 8,
            "idpost": "71444"
        },
        {
            "url": "https://tamanhhospital.vn/chuyen-khoa/noi-soi-tieu-hoa/",
            "category": "Nội soi tiêu hóa",
            "num_pages": 26,
            "idpost": "13253"
        },
        {
            "url": "https://tamanhhospital.vn/chuyen-khoa/khoa-tieu-hoa-gan-mat-tuy/",
            "category": "Gan mật tụy",
            "num_pages": 1,
            "idpost": None
        },
        {
            "url": "https://tamanhhospital.vn/chuyen-khoa/trung-tam-tim-mach/",
            "category": "Tim mạch",
            "num_pages": 32,
            "idpost": "13969"
        },
        {
            "url": "https://tamanhhospital.vn/chuyen-khoa/noi-than-kinh/",
            "category": "Nội thần kinh",
            "num_pages": 25,
            "idpost": "13970"
        },
        {
            "url": "https://tamanhhospital.vn/chuyen-khoa/noi-tiet-dai-thao-duong/",
            "category": "Nội tiết - Đái tháo đường",
            "num_pages": 25,
            "idpost": "13252"
        },
        {
            "url": "https://tamanhhospital.vn/chuyen-khoa/noi-co-xuong-khop/",
            "category": "Nội cơ xương khớp",
            "num_pages": 11,
            "idpost": "13255"
        },
        {
            "url": "https://tamanhhospital.vn/chuyen-khoa/tai-mui-hong/",
            "category": "Tai mũi họng",
            "num_pages": 18,
            "idpost": "13248"
        },
        {
            "url": "https://tamanhhospital.vn/chuyen-khoa/chan-thuong-chinh-hinh/",
            "category": "Chấn thương chỉnh hình",
            "num_pages": 32,
            "idpost": "13260"
        },
        {
            "url": "https://tamanhhospital.vn/chuyen-khoa/san-phu/",
            "category": "Sản phụ khoa",
            "num_pages": 42,
            "idpost": "13250"
        },
        {
            "url": "https://tamanhhospital.vn/chuyen-khoa/da-lieu/",
            "category": "Da liễu",
            "num_pages": 20,
            "idpost": "80342"
        },
        {
            "url": "https://tamanhhospital.vn/chuyen-khoa/noi-tong-hop/",
            "category": "Nội tổng hợp",
            "num_pages": 4,
            "idpost": "13251"
        },
        {
            "url": "https://tamanhhospital.vn/chuyen-khoa/nhi/",
            "category": "Nhi",
            "num_pages": 19,
            "idpost": "13256"
        },
        {
            "url": "https://tamanhhospital.vn/chuyen-khoa/so-sinh/",
            "category": "Sơ sinh",
            "num_pages": 6,
            "idpost": "13249"
        },
        {
            "url": "https://tamanhhospital.vn/chuyen-khoa/tiet-nieu/",
            "category": "Tiết niệu",
            "num_pages": 33,
            "idpost": "13247"
        },
        {
            "url": "https://tamanhhospital.vn/chuyen-khoa/ung-buou/",
            "category": "Ung bướu",
            "num_pages": 20,
            "idpost": "13967"
        },
        {
            "url": "https://tamanhhospital.vn/chuyen-khoa/noi-ho-hap/",
            "category": "Nội hô hấp",
            "num_pages": 5,
            "idpost": "13254"
        },
        {
            "url": "https://tamanhhospital.vn/chuyen-khoa/trung-tam-xet-nghiem/",
            "category": "Trung tâm xét nghiệm",
            "num_pages": 4,
            "idpost": "13246"
        },
        {
            "url": "https://tamanhhospital.vn/chuyen-khoa/chan-doan-hinh-anh/",
            "category": "Chẩn đoán hình ảnh",
            "num_pages": 11,
            "idpost": "13261"
        },
        {
            "url": "https://tamanhhospital.vn/chuyen-khoa/trung-tam-te-bao-goc/",
            "category": "Tế bào gốc",
            "num_pages": 3,
            "idpost": "13236"
        },
        {
            "url": "https://tamanhhospital.vn/chuyen-khoa/duoc/",
            "category": "Dược",
            "num_pages": 2,
            "idpost": "13971"
        },
        {
            "url": "https://tamanhhospital.vn/chuyen-khoa/nam-hoc/",
            "category": "Nam học",
            "num_pages": 33,
            "idpost": "14796"
        },
        {
            "url": "https://tamanhhospital.vn/chuyen-khoa/cap-cuu-hoi-suc-tich-cuc/",
            "category": "Cấp cứu",
            "num_pages": 7,
            "idpost": "13262"
        },
        {
            "url": "https://tamanhhospital.vn/chuyen-khoa/kham-benh/",
            "category": "Khám bệnh",
            "num_pages": 28,
            "idpost": "13258"
        }
    ])