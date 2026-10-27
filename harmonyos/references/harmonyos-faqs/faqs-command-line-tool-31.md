---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-31
title: 使用hdc shell param命令查询软件版本报错
breadcrumb: FAQ > DevEco Studio > 命令行工具 > 使用hdc shell param命令查询软件版本报错
category: harmonyos-faqs
scraped_at: 2026-10-28T07:49:03+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a491b2c45f744c2f31055cff85f8f9e4e2fb22ba94b508ac17fb39d16b1df2dd
---

## 问题现象

执行hdc shell param get const.product.software.version.name命令报错：Get parameter "xxx" fail! errNum is:106!

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/8tKiUuZzTqqBT3zmOPD6LA/zh-cn_image_0000002658808993.png "点击放大")

## 解决方案

原因：该命令是查询设备的软件版本，报错的原因是设备不支持该命令，不同的手机支持的查询命令不同。

解决方案：

1. 执行hdc list targets保证设备连接正确。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/b_Lr1yBVQVKr4kFeci4hBg/zh-cn_image_0000002628409728.png)
2. 进入hdc shell模式，执行param get | grep "const.product.software"命令，查找该设备所支持的命令参数，然后基于返回的结果进行软件版本的查看。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/nX4wJNmYQI-Yf-Nqab1iVg/zh-cn_image_0000002628569630.png "点击放大")

## 总结

hdc shell命令在不同的设备支持情况可能会有差异，使用hdc shell param get命令可以获取该设备的支持情况，比如使用const.product字段可以查询API版本、软件版本、硬件版本等信息。
