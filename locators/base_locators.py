'''Общие локаторы.'''

# Находит кнопку по точному тексту
BUTTON = '//button[text()="{}"]'

# Находит поле ввода по плейсхолдеру
INPUT_FIELD = '//input[@placeholder="{}"]'

# Находит div по части класса
DIV_CLS_CONTAINS = '//div[contains(@class, "{}")]'

# Находит div с точным текстом
TEXT_IN_DIV = '//div[text()="{}"]'

# Находит ссылку по части класса (с подстановкой в середину)
A_CLS_CONTAINS = '//a[contains(@class, "Logo{}")]'