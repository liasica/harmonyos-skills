---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-141
title: 编译报错“The type of target device does not match the device type configured by module：xxx”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The type of target device does not match the device type configured by module：xxx”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:53+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:04c3cdec7c8b0a18681175852c457438c5cfa0816e8543b5aaa653e493f0dfb7
---

**错误描述**

指定target设备的类型与模块配置的设备类型不匹配。

**可能原因**

指定target设备的类型与模块配置的设备类型不匹配。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/bTKPbsMNQyWsO2RLaT_D2A/zh-cn_image_0000002194158392.png)

**解决措施**

1. 确保module目录的build-profile.json5文件中targets下指定的设备类型包含所需的设备类型。
2. 确保module目录下src/main/module.json5中配置的deviceTypes字段包含所需的类型。
3. 检查hvigorfile.ts或[Hvigor脚本文件](../harmonyos-guides/ide-hvigor-life-cycle.md#section810245135914)是否包含任何可能更改模块deviceTypes设置的代码。
