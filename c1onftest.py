import pytest
import time

from selenium import webdriver


@pytest.fixture
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.jd.com')

    def teardown():
        time.sleep(4)
        driver.quit()

    request.addfinalizer(teardown)

    return driver
