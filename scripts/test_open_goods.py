import time

import allure
import pytest
from selenium import webdriver

from page.page import Page
from scripts import tools


class TestOpenGoods:
    @pytest.fixture(params=['Chrome', 'Firefox'], autouse=True)
    def setup(self, request):
        self.driver = eval('webdriver.%s()' % request.param)
        # self.driver = webdriver.Chrome()
        self.driver.get("https://www.jd.com/")
        self.driver.maximize_window()
        # 先固定写
        self.page = Page(self.driver)

        def teardown():
            time.sleep(2)
            self.driver.quit()

        request.addfinalizer(teardown)

    # def teardown(self):
    #     time.sleep(5)
    #     self.driver.quit()
    @allure.title("截图功能测试")
    @pytest.mark.parametrize('args', tools.analyse_data('./data/search_data.yaml', 'test_search'))  # 利用了yaml数据
    def test_open_goods(self, args):
        """
        这个用例测试京东网页商品界面的截图功能
        :param args:
        :return:
        """
        allure.attach.file('./image/2019-08-24-18_23_48.png', attachment_type=allure.attachment_type.PNG)
        self.page.search.input_goods_name(args['item'])
        self.page.search.click_search()
        self.page.search.click_goods(args['index'])
        self.page.search.switch_new_tab()
        self.page.search.shot_goods()
