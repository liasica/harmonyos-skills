---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-39
title: 单元测试如何创建ArkTS测试用例
breadcrumb: FAQ > DevEco Studio > 应用测试 > 单元测试如何创建ArkTS测试用例
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1d68da8a1be5d7b976a719b70329c973d767b4fcaaac24781e411a83ea6a7223
---

## 问题现象

在代码内部使用Show Context Actions创建单元测试用例时，提示No context actions available at this location。

## 背景知识

* [Instrument Test](../harmonyos-guides/ide-instrument-test.md)的测试用例存放在ohosTest测试目录下，需要运行在设备或模拟器上。
* [Local Test](../harmonyos-guides/ide-local-test.md)的测试用例存放在test测试目录下，不需要运行在设备或模拟器上。

## 问题定位

* 如果创建的是Instrument Test用例：
  1. 排查工程中是否存在“src/ohosTest”路径；

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/ho4RjWKWR06Lpd1gFcP6dg/zh-cn_image_0000002628569540.png?HW-CC-KV=V1&HW-CC-Date=20261112T233145Z&HW-CC-Expire=31536000000&HW-CC-Sign=34D86AC6253369FEF7D2F665644436C8A33972DDA2A83028DA616ABC48700897 "点击放大")
  2. 点击Settings->Editor->Intentions->JavaScript，查看是否勾选“Create Instrument Test”；

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/Ljrs8t9ZRiq9Rlhug9d5YA/zh-cn_image_0000002658928865.png?HW-CC-KV=V1&HW-CC-Date=20261112T233145Z&HW-CC-Expire=31536000000&HW-CC-Sign=7F5DAF09A1E8A60ECBA38F9B8B0E16324EBBA1C3881EE1C9A02CBB1F2EC9C1E4 "点击放大")
* 如果创建的是Local Test用例：
  1. 排查是否存在[代码测试](../harmonyos-guides/ide-code-test.md)中Local Test的相关约束与限制；
  2. 排查工程中是否存在“src/test”路径；

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/BZCWF70ES2ihUSDDn9ad-A/zh-cn_image_0000002628409650.png?HW-CC-KV=V1&HW-CC-Date=20261112T233145Z&HW-CC-Expire=31536000000&HW-CC-Sign=D47F9FB9272A47039DCF557D26BF23D3CBCFBE9BFCCD2ADCFB481CF44A7E05DC "点击放大")
  3. 点击Settings->Editor->Intentions->JavaScript，查看是否勾选“Create Local Test”；

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/n17cMpYjRje_-pYXab-PCA/zh-cn_image_0000002658808911.png?HW-CC-KV=V1&HW-CC-Date=20261112T233145Z&HW-CC-Expire=31536000000&HW-CC-Sign=1BD837F84C5922E37D1290E80D262E9B0EA1A9ED91B7453D237E3AEF01A07D28 "点击放大")

## 分析结论

IDE中未设置允许创建“Create Instrument Test”或“Create Local Test”。

## 修改建议

打开IDE，点击Settings->Editor->Intentions->JavaScript，勾选“Create Instrument Test”和“Create Local Test”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/_X_cSnH9RAuWIOGKrcRLvA/zh-cn_image_0000002628569542.png?HW-CC-KV=V1&HW-CC-Date=20261112T233145Z&HW-CC-Expire=31536000000&HW-CC-Sign=B2C47FE458A2D8614DA7EBFCDD28933D6B5F3497EB810B5B8EBE61EB31A02C05 "点击放大")

## 总结

在创建Local Test用例时需要关注约束与限制；IDE中需要设置允许创建“Create Instrument Test”或“Create Local Test”。
