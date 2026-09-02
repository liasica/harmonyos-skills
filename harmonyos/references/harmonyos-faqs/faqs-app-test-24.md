---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-24
title: PyCharm运行Hypium项目报错“测试用例的设备条件不满足”或者“required device does not exist”如何解决
breadcrumb: FAQ > DevEco Studio > 应用测试 > PyCharm运行Hypium项目报错“测试用例的设备条件不满足”或者“required device does not exist”如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:63d5a04eaec354f774088627b41f74c705696a3fbf3b087c87daba315745a075
---

## 问题现象

cmd命令行可以连接到设备，UiViewer也可以连接设备。但是执行用例出现如下报错信息：

* 提示“Test source required 1 devices, actually 0 devices were found [Suggestions]测试用例的设备条件不满足”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/8WfeLszcQVi1aDkYmEg6iA/zh-cn_image_0000002628409554.png "点击放大")
* 提示“required device does not exist”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/JHnS85HIShSmXywYMqnqzg/zh-cn_image_0000002628569452.png "点击放大")

## 背景知识

[DevEco Testing Hypium](../harmonyos-guides/hypium-python-guidelines.md#section16890204264419)以下简称（Hypium）是HarmonyOS平台的UI自动化测试框架，支持开发者使用python语言为应用编写UI自动化测试脚本。

## 问题定位

* 检查本地设备实际是否存在、系统环境变量[OHOS\_HDC\_SERVER\_PORT](../harmonyos-guides/hdc.md#ohos_hdc_server_port)的hdc端口配置。
* 检查当前user\_config.xml中是否设置了设备的sn，设备的sn是否实际存在。
* 检查用例的json文件请求的设备类型type字段是否正确。
* 检查json中请求的设备label类型是否正确。

## 分析结论

如果“hdc list targets”命令查询到设备，但Hypium框架运行报错设备未连接，排查以下原因：

* 系统环境变量OHOS\_HDC\_SERVER\_PORT配置的hdc端口非默认端口8710。
* 当前user\_config.xml设置的设备sn不存在。
* 用例的json文件type字段与当前设备不匹配。
* 用例的json文件设备label字段与当前设备不匹配。

## 修改建议

* 将OHOS\_HDC\_SERVER\_PORT环境变量删除后重启PyCharm。
* user\_config.xml文件sn不设置或者修改为当前设备sn，type类型和label类型按实际使用设备配置正确。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/KMLeCDzjRJKg9XZsffCY8A/zh-cn_image_0000002658928769.png "点击放大")
* 用例的json文件type类型配置正确。

  如下图所示，该用例请求了两个设备，一个为HarmonyOS设备，一个为其他平台设备。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/Y_QNd9RjQJyGVT_LBOqzzQ/zh-cn_image_0000002658808823.png "点击放大")
* 用例的json文件设备label类型配置每个设备对应的设备类型。如果用例可以在任何设备上运行，label字段不需要填。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/JmFJpMU8RlOYs5mNHdqYwQ/zh-cn_image_0000002628409556.png "点击放大")

  | label类型 | 设备 |
  | --- | --- |
  | phone | 手机 |
  | car | 车机 |
  | tv | 电视 |
  | watch | 手表 |
  | tablet | 平板 |
  | 2in1 | PC |

## 常见FAQ

Q：如何获取对应的设备类型？

A：通过hdc命令

```shell
hdc shell param get const.product.devicetype
```
