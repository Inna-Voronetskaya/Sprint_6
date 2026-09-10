from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def get_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click_element(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            element.click()
        except TimeoutException:
            element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def fill_form_field(self, locator, text, *keys):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.clear()
        element.send_keys(text)
        for key in keys:
            element.send_keys(key)

    def get_text(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).text

    def is_element_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_new_window(self):
        current = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            if handle != current:
                self.driver.switch_to.window(handle)
                break

    def wait_for_number_of_windows(self, expected_count, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.number_of_windows_to_be(expected_count)
        )