import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=30.0, poll=1.0):
        """
        根据元素特征（元组）寻找对应的一个元素
        :param feature: 特征
        :param timeout: 超时时间，默认10秒
        :param poll: 频率，默认1秒
        :return: 找到的元素
        """
        by, value = feature  # feature是个元组
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))

    def find_elements(self, feature, timeout=20.0, poll=1.0):
        """
        根据元素特征（元组）寻找对应的一组元素
        :param feature: 特征
        :param timeout: 超时时间，默认10秒
        :param poll: 频率，默认1秒
        :return: 找到的元素
        """
        by, value = feature
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(by, value))

    def click(self, feature):
        """
        根据特征，寻找元素，并点击
        :param feature: 特征
        """
        self.find_element(feature).click()

    def input(self, feature, content):
        """
        根据特征，寻找元素，并输入对应的文字
        :param feature: 特征
        :param content: 文字
        """
        self.clear(feature)
        self.find_element(feature).send_keys(content)

    def clear(self, feature):
        """
        根据特征，寻找元素，并清空文字
        :param feature: 特征
        """
        self.find_element(feature).clear()

    def screen_shot(self):
        """
        屏幕截图，保存在image文件夹中
        :return: 是否截图成功
        """
        # 以当前时间为截图命名
        picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

        return self.driver.get_screenshot_as_file('D:\\desktop\\unittest\\image\\' + picture_time + '.png')

    def is_feature_exits(self, feature):
        """
        根据 元素的特征 判断这个元素是否存在
        :param feature:
        :return:
        """
        try:
            self.find_element(feature)
            return True
        except Exception:
            return False

    # 切换窗口
    def switch_handle(self):
        current_handle = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        for handles in all_handles:
            if current_handle != handles:
                self.driver.switch_to.window(handles)




    # --------------------------------- mobile only ---------------------------------

    def press_back(self):
        """
        按返回键
        """
        self.driver.press_keycode(4)

    def press_enter(self):
        """
        按回车键
        """
        self.driver.press_keycode(66)

    def find_toast(self, message):
        """
        根据 部分 toast内容获取全部toast内容
        :param message: 部分内容
        :return:
        """
        toast_xpath = By.XPATH, "//*[contains(@text,'%s')]" % message
        print(toast_xpath)
        return self.find_element(toast_xpath, timeout=3, poll=0.1).text

    def is_toast_exits(self, message):
        """
        根据 部分 toast内容判断这个toast是否存在
        :param message:
        :return:
        """
        try:
            self.find_toast(message)
            return True
        except TimeoutException:
            return False

    def is_feature_exist_with_scroll(self, feature):
        """
        边滑边找某元素是否存在，直到停止
        :param feature: 元素
        :return:
        """
        old = ""
        while True:
            try:
                old = self.driver.page_source
                self.find_element(feature)
                return True
            except Exception:
                # 滑动操作

                self.scroll_page_one_time()

                if self.driver.page_source == old:
                    print("滑动到底部了")
                    return False

    def scroll_page_one_time(self, dir="up"):
        """
        根据方向，滑动一次（半屏）
        :param dir:
            up：从下往上
            down：从上往下
            left：从右往左
            right：从左往右
        :return:
        """
        screen_width = self.driver.get_window_size()["width"]
        screen_height = self.driver.get_window_size()["height"]

        bottom_x = screen_width * 0.5
        bottom_y = screen_height * 0.75
        top_x = bottom_x
        top_y = screen_height * 0.25
        left_x = screen_width * 0.25
        left_y = screen_height * 0.5
        right_x = screen_width * 0.75
        right_y = left_y

        if dir == "up":
            self.driver.swipe(bottom_x, bottom_y, top_x, top_y, 3000)
        elif dir == "down":
            self.driver.swipe(top_x, top_y, bottom_x, bottom_y, 3000)
        elif dir == "left":
            self.driver.swipe(right_x, right_y, left_x, left_y, 3000)
        elif dir == "right":
            self.driver.swipe(left_x, left_y, right_x, right_y, 3000)
        else:
            raise Exception("请传入正确的参数 up/down/left/right")

# --------------------------------- mobile only ---------------------------------
