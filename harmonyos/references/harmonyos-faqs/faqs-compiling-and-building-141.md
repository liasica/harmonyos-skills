---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-141
title: 编译报错“The type of target device does not match the device type configured by module：xxx”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The type of target device does not match the device type configured by module：xxx”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:40+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:4f864f5d6dfbdecec9b02d8b880320e5b155130558ef7f6e92e41b0c413e4f80
---

**错误描述**

指定target设备的类型与模块配置的设备类型不匹配。

**可能原因**

指定target设备的类型与模块配置的设备类型不匹配。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/bTKPbsMNQyWsO2RLaT_D2A/zh-cn_image_0000002194158392.png?HW-CC-KV=V1&HW-CC-Date=20260428T002939Z&HW-CC-Expire=86400&HW-CC-Sign=D9AAF4C2EBFCD9783D0DEC193488EDBF851EC72BD4CACB2019512BA55C1CCD38)

**解决措施**

1. 确保module目录的build-profile.json5文件中targets下指定的设备类型包含所需的设备类型。
2. 确保module目录下src/main/module.json5中配置的deviceTypes字段包含所需的类型。
3. 检查hvigorfile.ts或[Hvigor脚本文件](../harmonyos-guides/ide-hvigor-life-cycle.md#section810245135914)是否包含任何可能更改模块deviceTypes设置的代码。
