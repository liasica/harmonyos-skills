---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-25
title: 使用Hypium自动化验证xpath控件的唯一性
breadcrumb: FAQ > DevEco Studio > 应用测试 > 使用Hypium自动化验证xpath控件的唯一性
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2542304d71e8d615a6b809cb6093ad4dd894bdbac8714cd2da18658fdebc1650
---

## 问题现象

Hypium自动化在定位器中，通过XPath语法写的XPath路径，在定位器的哪里验证该XPath是否唯一？

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/tN7nnQO-R5WjV8RIbrWE0Q/zh-cn_image_0000002628569454.png "点击放大")

## 背景知识

* [DevEco Testing Hypium](../harmonyos-guides/hypium-python-guidelines.md#section16890204264419)插件会在PyCharm界面右边缘的ToolWindow区域生成UiViewer标签，点击后会展开UiViewer面板。UiViewer功能目前分为4个界面：设备选择界面、单设备控件查看界面、单设备投屏界面、双设备投屏界面。
* XPath方式查找匹配的控件：部分控件没有唯一定位的属性，同时通过相对定位的方式也无法准确定位，此时可以使用XPath语法来进行更精确的控件定位。使用BY.xpath匹配器可以支持通过XPath语法来查找控件。详情请参考[API使用方法](../harmonyos-guides/hypium-python-guidelines.md#section4598236435)。

## 解决方案

* 用户可以根据控件的key、text、type内容来搜索指定控件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/tq0CPbjlSduaW-r_3NKnHQ/zh-cn_image_0000002658928773.png "点击放大")
* 通过API方法实现XPath语法验证控件是否唯一。

  ```python
  from devicetest.core.test_case import TestCase, Step, MESSAGE
  from hypium import UiDriver, BY
  class TC_001(TestCase):
      def __init__(self, configs):
          self.TAG = self.__class__.__name__
          super().__init__(self.TAG, configs)
          self.driver = UiDriver(self.device1)
          self.driver_width, self.driver_height = self.driver.get_display_size()
      def setup(self):
          Step('1.回到桌面')
          self.driver.swipe_to_home()
      def process(self):
          Step('2.启动设置应用')
          self.driver.start_app("com.huawei.hmos.settings")
          Step("步骤1:验证控件是否存在且唯一")
          comp = self.driver.find_all_components(BY.xpath("//*[@text='WLAN']"))
          MESSAGE('component is ' + str(comp))
      def teardown(self):
          pass
  ```

## 常见FAQ

Q：WebView页面是否支持验证XPath表达式？

A：WebView页面可以通过浏览器自带的检测功能进行检测，按F12打开浏览器开发者工具按Ctrl+F键查找。

Q：使用“hdc shell uitest dumpLayout”指令获取到的控件树如何实现UI自动化？

A：控件树中类型为空串的节点代表当前的屏幕信息，类型为root和WindowScene和当前屏幕的对应关系可以通过UiViewer查看，如果想实现UI自动化，推荐使用[DevEco Testing Hypium](../harmonyos-guides/hypium-python-guidelines.md#section16890204264419)的UiViewer插件，可以对控件树进行可视化和获取控件的信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/8qQAGBrARfClfmPd-uLxQA/zh-cn_image_0000002658808825.png "点击放大")
