---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-22
title: Hypium连接设备提示“选中设备中包含不兼容的设备”
breadcrumb: FAQ > DevEco Studio > 应用测试 > Hypium连接设备提示“选中设备中包含不兼容的设备”
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2d9f152eb9c6ec3d5922a9b24dc7ff5168247f5984e2dce884cb18bd0485a717
---

## 问题现象

手机连接上电脑，执行hdc list targets可以识别到设备，但使用Hypium的UiViewer功能时提示“选中设备中包含不兼容的设备！”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/c65j7pmoRUawFCTCvap8Lw/zh-cn_image_0000002658928763.png)

## 背景知识

[DevEco Testing Hypium](../harmonyos-guides/hypium-python-guidelines.md#section16890204264419)插件中内置了UiViewer功能，能够对设备当前页面的控件元素进行解析并展示。UiViewer功能目前分为4个界面：设备选择界面、单设备控件查看界面、单设备投屏界面、双设备投屏界面。

## 问题定位

* 检查hdc、Hypium插件、设备驱动程序已正确安装。执行hdc list targets查看设备是否能够被正确识别。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/hL0YFx_jRvShy_NJSnXE6Q/zh-cn_image_0000002658808817.png)
* 执行hdc shell uitest --version命令，查看版本号是否大于4.1.4.0。如下图显示的4.0.4.0版本不支持UiViewer查看设备。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/CFOZtL_vSmemejjWXBTNow/zh-cn_image_0000002628409550.png)
* 执行hdc -v命令，查看版本号是否在3.0.0及以上。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/j8i286g1SS6Bi5uopVXMww/zh-cn_image_0000002628569448.png)
* 检查Hypium插件是否为6.0.0 Release及以上版本：打开Pycharm，点击File -> Settings -> Plugins进行查看。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/oOzE5hHiRz2ZImMgjz8pbw/zh-cn_image_0000002658928765.png)

## 分析结论

Hypium连接设备提示“选中设备中包含不兼容的设备”可能有以下原因：

* uitest版本小于4.1.4.0。
* hdc版本在3.0.0及以下。
* Hypium插件未升级到6.0.0 Release及以上版本。

## 修改建议

* 查看获取到系统uitest的版本结果，如果小于4.1.4.0版本，需要升级手机系统，手机设置页面检查更新，具体版本请查看[各版本支持设备型号清单](../harmonyos-releases/support-device.md)。如遇版本无法升级，可以[新建工单](https://developer.huawei.com/consumer/cn/support/feedback/#/)进行申请。手机系统升级对应IDE也需要升级，IDE和手机ROM需要配套使用。详情请参考HarmonyOS套件配套信息[所有HarmonyOS版本](../harmonyos-releases/overview-allversion.md)。
* 查看获取到hdc的版本结果，如果低于3.0.0版本，需要参考[环境准备](../harmonyos-guides/hdc.md#环境准备)的内容进行hdc版本的升级。
* Hypium插件需要升级到6.0.0 Release及以上版本，访问华为开发者联盟官网下载[DevEco Testing Hypium安装包](https://developer.huawei.com/consumer/cn/download/deveco-testing-hypium)。
* 确认以上信息已修改后，请重新授权连接设备，查看UiViewer页面查看设备、DevEco Testing投屏功能是否可以正常使用。

## 常见FAQ

Q：DevEco Testing Hypium调试脚本时，报错：ohos.exception.OHOSRpcPortNotFindError: [Environment-0303026] BIN(ABC) RPC listening。

A：需要使用HarmonyOS 5.0及以上版本。
