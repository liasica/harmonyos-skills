---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-31
title: DevEco Testing Hypium中的UiViewer使用中的常见问题和解决方案
breadcrumb: FAQ > DevEco Studio > 应用测试 > DevEco Testing Hypium中的UiViewer使用中的常见问题和解决方案
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:46d9fa5d11cb391365f4413058146c48609921c6c39ec2e3e62286d76c2b2d82
---

## 问题现象

使用[DevEco Testing Hypium](../harmonyos-guides/hypium-python-guidelines.md#section16890204264419)插件展开UiViewer功能面板，提示“获取视频流失败，请重新选择设备进入”，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/pFlVd5o7T-OzaFKGNehnsQ/zh-cn_image_0000002628409626.png "点击放大")

## 背景知识

PyCharm界面右侧栏的toolWindow区域可见UiViewer标签，点击后展开UiViewer面板。UiViewer功能目前分为4个界面：设备选择界面、单设备控件查看界面、单设备投屏界面、双设备投屏界面。详情请参考[安装向导](../harmonyos-guides/hypium-python-guidelines.md#section191615399595)的UiViewer功能模块。

## 问题定位

* 查看插件版本是否为Hypium的新版本。

  打开PyCharm的settings->Plugins查看版本号。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/fP_1gORaRNaqhMzSH6tyNA/zh-cn_image_0000002658808885.png "点击放大")
* 查看设备视频流设置。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/qKI0Z9LJSaiVHLHw3UVN1w/zh-cn_image_0000002628569518.png "点击放大")

## 分析结论

* 插件版本未更新，导致投屏失败。
* 无法获取设备视频流。

## 修改建议

* 更新当前插件版本为适配Hypium新版本。

  访问华为开发者联盟官网下载[DevEco Testing Hypium安装包](https://developer.huawei.com/consumer/cn/download/deveco-testing-hypium)，下载解压后找到其中的hypium-5.0.7.200.zip(请以实际版本号为准)。DevEco Testing Hypium离线安装包请参考[安装向导](../harmonyos-guides/hypium-python-guidelines.md#section191615399595)的安装包离线安装模块。
* 使用视频流投屏模式设置。

  将PyCharm的settings->DevEco Testing Hypium->UiViewer的是否使用视频流投屏模式设置为否，再重新使用插件进行手机投屏。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/rO4jkl21TNe9SCmSD7LVIg/zh-cn_image_0000002658928841.png "点击放大")

## 常见FAQ

Q：PyCharm专业版使用DevEco Testing Hypium时，UiViewer无法看到设备如何解决？

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/IQVwsDIzQSuHuI1pwgiUwA/zh-cn_image_0000002628409628.png "点击放大")

A：检查系统环境变量[OHOS\_HDC\_SERVER\_PORT](../harmonyos-guides/hdc.md#ohos_hdc_server_port)：如果电脑的8710端口已经被使用或希望使用其他端口，可以通过添加环境变量OHOS\_HDC\_SERVER\_PORT到系统环境变量中来修改服务器进程启动时监听的端口号，设置完之后重启PyCharm。
