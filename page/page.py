class Page:

    def __init__(self, driver):
        self.driver = driver

    def __getattr__(self, name):
        """
        调用page中的页面时调用该方法，当使用点号获取属性时如果不存在就自动调用 __getattr__ 方法
        :param name: 被调用的属性
        :return: 该属性的值
        """

        """
        如果在脚本中调用了 page.login 页面，则参数 name 为 "login"
        如果在脚本中调用了 page.login_hello 页面，则参数 name 为 "login_hello"
        根据下划线分割，"login" 结果为 ["login"]，"login_hello" 结果为 ["login", "hello"]
        列表中的每个单词首字母转化为大写，并添加 "Page"
        page为 "LoginPage" 或 "LoginHelloPage"
        """
        page_name = ""
        for i in name.split("_"):
            page_name += i.capitalize()
        page_name += "Page"

        # 动态导入 login_page/login_hello_page 中的 LoginPage/LoginHelloPage
        exec("from page." + name + "_page import " + page_name)

        # 动态创建该对象并返回  动态执行LoginPage(self.driver)代码
        return eval(page_name + "(self.driver)")     
