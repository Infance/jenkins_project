import time

import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SearchPage(BaseAction):
    # 商品搜索框
    goods_name_search_field = By.XPATH, '//*[@id="key"]'

    # 搜索按钮   //*,代表选取文档中的所有元素    python双引号里不能有双引号，外层要用单引号
    search_button = By.XPATH, '//*[@id="search"]/div/div[2]/button'

    # 输入搜索商品
    @allure.step(title='输入商品名称')
    def input_goods_name(self, items):
        self.input(self.goods_name_search_field, items)

    # 点击搜索按钮
    @allure.step('点击搜索框')
    def click_search(self):
        self.click(self.search_button)

    # 点击第N个商品
    @allure.step('点击商品')
    def click_goods(self, index):
        my_path = '//*[@id="J_goodsList"]/ul/li[%s]' % index
        goods_picture = By.XPATH, my_path
        self.click(goods_picture)

    # 切换标签页，使用句柄
    def switch_new_tab(self):
        self.switch_handle()

    # 截图
    @allure.step('截图保存在/image文件夹下')
    def shot_goods(self):
        time.sleep(3)
        self.screen_shot()


