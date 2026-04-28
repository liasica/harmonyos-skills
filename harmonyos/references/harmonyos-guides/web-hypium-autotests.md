---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-hypium-autotests
title: 使用Hypium实现ArkWeb自动化测试
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > Web调试维测 > 使用Hypium实现ArkWeb自动化测试
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:08+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:884a0abd90a71b78ffe729d4a3010e54a8927541661fddf929f571c2edcb12cc
---

## 概述

ArkWeb页面支持使用Hypium集成Selenium框架、ChromeDriver驱动进行UI自动化测试。

## 环境配置

1.Hypium环境搭建

参考：[应用UI测试（基于Python）](hypium-python-guidelines.md)。

2.安装Selenium

Selenium主要用于Web应用程序的自动化测试，核心功能是模拟用户在浏览器中的操作，例如点击按钮、输入文本、导航页面等。

```
1. pip install selenium
```

3.集成ChromeDriver驱动

ChromeDriver充当了Selenium WebDriver和Web页面之间的中介。通过Selenium发送命令时，ChromeDriver会将这些命令转换为Web内核能够理解的协议，并将响应返回给Selenium。ArkWeb基于谷歌Chromium内核开发，系统版本与Chromium版本的对应关系参考：ArkWeb简介[约束与限制](web-component-overview.md#约束与限制)。访问ChromeDriver官方网站[ChromeDriver下载|Chrome for Developers](https://developer.chrome.google.cn/docs/chromedriver/downloads?hl=zh-cn)，获取与Chromium版本对应的ChromeDriver。

首先将ChromeDriver集成到测试工程的resource文件夹下，然后调用WebDriverSetupTool类中的set\_chromedriver\_exe\_path方法指定chromedriver文件的存放路径或者调用set\_chromedriver\_exe\_search\_path方法指定chromedriver所在文件夹的路径。

```
1. self.web_tools = WebDriverSetupTool(self.driver)
2. # 使用set_chromedriver_exe_path指定chromedriver路径，需指定到对应版本的可执行chromedriver文件
3. self.web_tools.set_chromedriver_exe_path(r"D:\WebAutoTest\resource\web_debug_tools\chromedriver_132\chromedriver.exe")
```

```
1. self.web_tools = WebDriverSetupTool(self.driver)
2. # 使用set_chromedriver_exe_search_path方法指定chromedriver所在文件夹，Hypium在指定的文件夹寻找对应版本的chromedriver文件
3. self.web_tools.set_chromedriver_exe_search_path(r"D:\WebAutoTest\resource\web_debug_tools")
```

说明

* 使用set\_chromedriver\_exe\_search\_path方法指定chromedriver所在文件夹的路径时，下层文件夹命名规则为chromedriver\_版本号，参考下图。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/ok5s2VU8RaOsXT6OrRLfgg/zh-cn_image_0000002552958256.png?HW-CC-KV=V1&HW-CC-Date=20260427T234107Z&HW-CC-Expire=86400&HW-CC-Sign=80F17CCD616F216E39B644C08B9AA637710A1AD0B6578B92174A9DE3D4270B05)

## 示例代码

参考以下代码完成ArkWeb页面的自动化测试，先初始化Selenium的webdriver，后通过webdriver与Web页面交互的API，实现导航页面、查找页面元素操作。

webdriver更多使用方法参考Selenium官方文档：[驱动会话 | Selenium](https://www.selenium.dev/zh-cn/documentation/webdriver/drivers/)。

```
1. from devicetest.core.test_case import TestCase, Step, CheckPoint
2. from hypium import UiDriver, BY
3. from hypium.webdriver.webdriver_setup_tool import WebDriverSetupTool

5. class ArkWeb_AutoTests(TestCase):
6. def __init__(self, configs):
7. self.TAG = self.__class__.__name__
8. TestCase.__init__(self, self.TAG, configs)
9. self.driver = UiDriver(self.device1)
10. self.driver_width, self.driver_height = self.driver.get_display_size()
11. self.web_tools = WebDriverSetupTool(self.driver)
12. # 设置chromedriver存放路径
13. self.web_tools.set_chromedriver_exe_search_path(r"D:\WebAutoTest\resource\web_debug_tools")
14. # 使用应用包名连接到指定应用的webview页面
15. self.web_tools.connect("com.huawei.hmos.browser")
16. # 初始化Selenium的webdriver
17. self.web_driver = self.web_tools.driver

19. def setup(self):
20. pass

22. def process(self):
23. # 导航页面：使用Selenium的webdriver访问https://developer.huawei.com/网站
24. self.web_driver.get("https://developer.huawei.com/")
25. # 查找页面元素：使用Selenium的webdriver查找页面ID为th的元素
26. self.web_driver.find_element(BY.ID, "th")

28. def teardown(self):
29. # 使用结束需要调用webdriver_setup_tool中的close方法关闭web_tools建立的连接
30. self.web_tools.close()
```
