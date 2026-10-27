---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-security-basic-quality-test-1
title: 如何定位安全基础质量测试检测不通过问题
breadcrumb: FAQ > DevEco Testing > 专项测试 > 安全基础质量测试 > 如何定位安全基础质量测试检测不通过问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:49:04+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:641e857b1eb048eae1dc592979ee3c26745e7e183a14e2f93961a01ebdec30dd
---

## 问题现象

使用DevEco Testing执行[安全基础质量测试](../harmonyos-guides/other-test.md#section2492910181110)，检测报告中部分检测项不通过，可以点击检测失败项后面的“查看”按钮，然后进入详情页中查看具体的报错详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/-ObAzGnMS0qvEqxMGRvgaw/zh-cn_image_0000002631296864.png "点击放大")

问题一：测试报告中“应用权限申请遵循最小化原则”测试结果不通过。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/gApspj-BSSGYJmO9iBdOeg/zh-cn_image_0000002631296866.png "点击放大")

问题二：测试报告中“应用所需权限必须在应用的配置文件中严格按照权限开发指导逐个声明”测试结果不通过。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/PcQ9iXt-Qg-R_x1vf5ETAg/zh-cn_image_0000002661496107.png "点击放大")

## 解决方案

问题一解决方案：

1. 查看问题描述中所列的异常权限：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/JvfKlE1TT2C66IdA9ACOgQ/zh-cn_image_0000002631137366.png "点击放大")
2. 在[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中requestPermissions字段下面找到问题描述所列的权限，在[应用权限列表](../harmonyos-guides/app-permissions.md)中查找权限名称：确认是否支持、权限是否废弃、权限拼写是否有误。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/BMzLKegoRKm3Wp1WXrg5jQ/zh-cn_image_0000002661496509.png)

问题二解决方案：

1. 查看问题描述中报错原因（以下为举例）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/q72JrVAbQeGHu-aDvwcTzw/zh-cn_image_0000002631137422.png "点击放大")
2. 在module.json5配置文件中查找该权限，因为ohos.permission.ACCESS\_BLUETOOTH是UserGrant权限，所以usedScene是必填项，需要补充usedScene属性。参考文档[声明权限](../harmonyos-guides/declare-permissions.md#在配置文件中声明权限)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/3LnNb9F6RiSorrPn-OvoOA/zh-cn_image_0000002661376615.png)

   权限类型确认可查看[应用权限列表](../harmonyos-guides/app-permissions.md)。
