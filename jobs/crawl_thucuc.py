
from core.crawlers.thu_cuc_crawler import ThucucCrawler

def crawl_thucuc():
    crawler = ThucucCrawler(is_multi_process=True)
    crawler.crawl([
        {
            "url": "https://benhvienthucuc.vn/song-khoe/tin-tuc-y-khoa/",
            "category": "Tin tức y khoa",
            "num_pages": 59,
        },
        {
            "url": "https://benhvienthucuc.vn/song-khoe/benh-co-xuong-khop/",
            "category": "Bệnh cơ xương khớp",
            "num_pages": 125,
        },
        {
            "url": "https://benhvienthucuc.vn/song-khoe/benh-gan-mat/",
            "category": "Bệnh gan mật",
            "num_pages": 82,
        },
        {
            "url": "https://benhvienthucuc.vn/song-khoe/san-khoa/",
            "category": "Sản khoa",
            "num_pages": 313,
        },
        {
            "url": "https://benhvienthucuc.vn/song-khoe/benh-ho-hap/",
            "category": "Bệnh hô hấp",
            "num_pages": 41,
        },
        {
            "url": "https://benhvienthucuc.vn/song-khoe/benh-tai-mui-hong/",
            "category": "Bệnh tai mũi họng",
            "num_pages": 96,
        },
        {
            "url": "https://benhvienthucuc.vn/song-khoe/benh-than-kinh/",
            "category": "Bệnh thần kinh",
            "num_pages": 131,
        },
        {
            "url": "https://benhvienthucuc.vn/song-khoe/benh-tiet-nieu/",
            "category": "Bệnh tiết niệu",
            "num_pages": 78,
        },
        {
            "url": "https://benhvienthucuc.vn/song-khoe/benh-tieu-hoa/",
            "category": "Bệnh tiêu hoá",
            "num_pages": 279,
        },
        {
            "url": "https://benhvienthucuc.vn/song-khoe/rang-ham-mat/",
            "category": "Răng hàm mặt",
            "num_pages": 127,
        },
        {
            "url": "https://benhvienthucuc.vn/song-khoe/benh-hau-mon-truc-trang/",
            "category": "Bệnh hậu môn – trực tràng",
            "num_pages": 19,
        },
        {
            "url": "https://benhvienthucuc.vn/song-khoe/benh-tim-mach/",
            "category": "Bệnh tim mạch",
            "num_pages": 69,
        },
        {
            "url": "https://benhvienthucuc.vn/song-khoe/benh-tre-em/",
            "category": "Bệnh trẻ em",
            "num_pages": 158,
        },
        {
            "url": "https://benhvienthucuc.vn/song-khoe/benh-ung-thu/",
            "category": "Bệnh ung thư",
            "num_pages": 214,
        },
        {
            "url": "https://benhvienthucuc.vn/song-khoe/benh-phu-khoa/",
            "category": "Bệnh phụ khoa",
            "num_pages": 67,
        },
        {
            "url": "https://benhvienthucuc.vn/song-khoe/benh-truyen-nhiem/",
            "category": "Bệnh truyền nhiễm",
            "num_pages": 19,
        },
        {
            "url": "https://benhvienthucuc.vn/song-khoe/benh-noi-tiet/",
            "category": "Bệnh nội tiết",
            "num_pages": 45,
        },
        {
            "url": "https://benhvienthucuc.vn/song-khoe/chan-doan-hinh-anh/",
            "category": "Chẩn đoán hình ảnh",
            "num_pages": 33,
        },
        {
            "url": "https://benhvienthucuc.vn/song-khoe/kham-suc-khoe/",
            "category": "Khám sức khoẻ",
            "num_pages": 54,
        },
        {
            "url": "https://benhvienthucuc.vn/song-khoe/tam-soat-ung-thu-song-khoe/",
            "category": "Tầm soát ung thư",
            "num_pages": 55,
        },
        {
            "url": "https://benhvienthucuc.vn/song-khoe/benh-ve-mat/",
            "category": "Bệnh về mắt",
            "num_pages": 74,
        },
        {
            "url": "https://benhvienthucuc.vn/song-khoe/benh-nam-khoa/",
            "category": "Bệnh nam khoa",
            "num_pages": 17,
        },
        {
            "url": "https://benhvienthucuc.vn/song-khoe/benh-da-lieu/",
            "category": "Bệnh da liễu",
            "num_pages": 17,
        },
        {
            "url": "https://benhvienthucuc.vn/song-khoe/vac-xin-tiem-chung/",
            "category": "Vắc xin tiêm chủng",
            "num_pages": 45,
        }
    ])