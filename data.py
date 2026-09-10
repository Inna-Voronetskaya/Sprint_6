# data.py

# data.py

class Urls:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru/'
    ORDER_PAGE = BASE_URL + 'order'
    DZEN_URL = 'https://dzen.ru/?yredirect=true'


class TestData:
    CUSTOMER_1 = {
        'name': 'Станислав',
        'last_name': 'Лем',
        'address': 'Кафедра Антропологии МГУ',
        'metro': 'Охотный Ряд',
        'phone': '84951234567',
    }
    
    RENT_1 = {
        'date': '31.12.2024',
        'days': 'сутки',
        'color': 'black',
        'comment': '',
    }
    
    CUSTOMER_2 = {
        'name': 'Аркадий',
        'last_name': 'Стругацкий',
        'address': 'г.Москва, отдел Звездной астрофизики ГАИШ МГУ',
        'metro': 'Университет',
        'phone': '84997654321',
    }
    
    RENT_2 = {
        'date': '01.01.2025',
        'days': 'семеро суток',
        'color': 'grey',
        'comment': 'Поскорей!',
    }


SCOOTER_FOR = 'Для кого самокат'
RENT = 'Про аренду'
CONFIRM_ORDER = 'Хотите оформить заказ?'
BOOKED = 'Заказ оформлен'