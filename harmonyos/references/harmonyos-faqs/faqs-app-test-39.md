---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-39
title: 单元测试如何创建ArkTS测试用例
breadcrumb: FAQ > DevEco Studio > 应用测试 > 单元测试如何创建ArkTS测试用例
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:58+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0891ae7ce89b8d25ce2203cf5c23187b71a914d70103c243f846344c0c43c256
---

## 问题现象

在代码内部使用Show Context Actions创建单元测试用例时，提示No context actions available at this location。

## 背景知识

* [Instrument Test](../harmonyos-guides/ide-instrument-test.md)的测试用例存放在ohosTest测试目录下，需要运行在设备或模拟器上。
* [Local Test](../harmonyos-guides/ide-local-test.md)的测试用例存放在test测试目录下，不需要运行在设备或模拟器上。

## 问题定位

* 如果创建的是Instrument Test用例：
  1. 排查工程中是否存在“src/ohosTest”路径；

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/GxmcvM6QRlqLI-2S9WaUCw/zh-cn_image_0000002628569540.png "点击放大")
  2. 点击Settings->Editor->Intentions->JavaScript，查看是否勾选“Create Instrument Test”；

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/WhnSAIpnTRyvQoJjJwltvw/zh-cn_image_0000002658928865.png "点击放大")
* 如果创建的是Local Test用例：
  1. 排查是否存在[代码测试](../harmonyos-guides/ide-code-test.md)中Local Test的相关约束与限制；
  2. 排查工程中是否存在“src/test”路径；

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/RbMARSoKRvaN0SWRPUu8Jg/zh-cn_image_0000002628409650.png "点击放大")
  3. 点击Settings->Editor->Intentions->JavaScript，查看是否勾选“Create Local Test”；

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/a0WpWk1JQt6kiFNc8o0YrA/zh-cn_image_0000002658808911.png "点击放大")

## 分析结论

IDE中未设置允许创建“Create Instrument Test”或“Create Local Test”。

## 修改建议

打开IDE，点击Settings->Editor->Intentions->JavaScript，勾选“Create Instrument Test”和“Create Local Test”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/MGnnPmMaRXC96D6_WTaGLw/zh-cn_image_0000002628569542.png "点击放大")

## 总结

在创建Local Test用例时需要关注约束与限制；IDE中需要设置允许创建“Create Instrument Test”或“Create Local Test”。
