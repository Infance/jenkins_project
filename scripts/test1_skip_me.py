import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestSkip:

    @pytest.mark.parametrize('name', ['小牛电动车',
                                      pytest.param('飞科剃须刀', marks=pytest.mark.skip),
                                      pytest.param('西门子冰箱', marks=pytest.mark.xfail()),
                                      pytest.param('小米手机6', marks=pytest.mark.skipif(3 > 4, reason='这是不可能的'))
                                      ])
    def test_skip_if(self, name, setup):
        WebDriverWait(setup, 20, 1).until(lambda x: x.find_element(By.XPATH, '//*[@id="key"]')).send_keys(name)
