from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):
    # 用户名输入框
    username_text_filed = By.NAME, "email"

    # 密码输入框
    password_text_filed = By.NAME, "password"

    # 登录模式的按钮
    change_login_type_button = By.XPATH, '//*[@id="lbNormal"]'

    # 登录的frame
    login_frame = By.TAG_NAME, "iframe"

    # 登录按钮
    login_button = By.ID, "dologin"

    # 输入 用户名输入框 hitfeat
    def input_username(self):
        self.driver.switch_to.frame(self.get_login_frame())
        self.input(self.username_text_filed, "hitfeat")
        self.driver.switch_to.default_content()

    # 输入 密码输入框 hitfeat123000
    def input_password(self):
        self.driver.switch_to.frame(self.get_login_frame())
        self.input(self.password_text_filed, "hitfeat123000")
        self.driver.switch_to.default_content()

    # 点击 切换登录模式的按钮
    def click_change_login_type(self):
        self.click(self.change_login_type_button)

    def get_login_frame(self):
        return self.find_element(self.login_frame)

    # 点击登录按钮
    def click_login(self):
        self.driver.switch_to.frame(self.get_login_frame())
        self.click(self.login_button)
        self.driver.switch_to.default_content()
