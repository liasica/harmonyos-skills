---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-security-basic-quality-test-1
title: 如何定位安全基础质量测试检测不通过问题
breadcrumb: FAQ > DevEco Testing > 专项测试 > 安全基础质量测试 > 如何定位安全基础质量测试检测不通过问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:59+08:00
doc_updated_at: 2026-06-30
content_hash: sha256:36f54235d09b716f7bf4d3a6a1d4d65c01be5b86bf0e37c0d5c9f395a6b209eb
---

## 问题现象

使用DevEco Testing执行[安全基础质量测试](../harmonyos-guides/other-test.md#section2492910181110)，检测报告中部分检测项不通过，可以点击检测失败项后面的“查看”按钮，然后进入详情页中查看具体的报错详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/VtGmXWbnS8qWOp9kTNBcgw/zh-cn_image_0000002631296864.png "点击放大")

问题一：测试报告中“应用权限申请遵循最小化原则”测试结果不通过。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/uq0WGp2fT3u1R7Q41fOPfw/zh-cn_image_0000002631296866.png "点击放大")

问题二：测试报告中“应用所需权限必须在应用的配置文件中严格按照权限开发指导逐个声明”测试结果不通过。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/-s7QHdrIRRqk41hGj9pwdA/zh-cn_image_0000002661496107.png "点击放大")

## 解决方案

问题一解决方案：

1. 查看问题描述中所列的异常权限：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/ncqlCOUNTrOgqiXViRksWg/zh-cn_image_0000002631137366.png "点击放大")
2. 在[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中requestPermissions字段下面找到问题描述所列的权限，在[应用权限列表](../harmonyos-guides/app-permissions.md)中查找权限名称：确认是否支持、权限是否废弃、权限拼写是否有误。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/vYsfBjhET3aN8nrLK6C1Ng/zh-cn_image_0000002661496509.png)

问题二解决方案：

1. 查看问题描述中报错原因（以下为举例）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/FPVrZnD2Sr6j8Qc9YC8lYg/zh-cn_image_0000002631137422.png "点击放大")
2. 在module.json5配置文件中查找该权限，因为ohos.permission.ACCESS\_BLUETOOTH是UserGrant权限，所以usedScene是必填项，需要补充usedScene属性。参考文档[声明权限](../harmonyos-guides/declare-permissions.md#在配置文件中声明权限)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/JgpMRAXETwGJOmZcgZP-qA/zh-cn_image_0000002661376615.png)

   权限类型确认可查看[应用权限列表](../harmonyos-guides/app-permissions.md)。
