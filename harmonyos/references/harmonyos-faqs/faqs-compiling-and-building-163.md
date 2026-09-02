---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-163
title: 编译报错“The permission under requestPermissions must be a value that is predefined within the SDK or a custom one that you have included under definePermissions.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The permission under requestPermissions must be a value that is predefined within the SDK or a custom one that you have included under definePermissions.”
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:0535569a4c3951775db3371b698cdbbc6af2ebffccb2740b0b7642190c53e9fe
---

**错误描述**

requestPermissions下的权限必须是SDK中预定义的值，或在definePermissions中定义的自定义值。

**可能原因**

在module.json5文件的requestPermissions中配置name时，使用了不存在的权限名称或者使用了当前版本不支持的权限。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/BmdimmurQH6iIRRsM-svAQ/zh-cn_image_0000002624638552.png)

**解决措施**

在module.json5文件的requestPermissions中配置name字段时，必须使用SDK中预定义的权限或在definePermissions下自定义的权限。如果使用了当前版本不支持的权限，建议升级API版本。

例如，若在DevEco Studio 6.0.0 Release版本使用了[ohos.permission.START\_WINDOW\_BELOW\_LOCK\_SCREEN](../harmonyos-guides/permissions-for-all.md#ohospermissionstart_window_below_lock_screen)权限，但该权限从API 21开始支持，建议开发者前往[下载中心](https://developer.huawei.com/consumer/cn/download/)将DevEco Studio更新至DevEco Studio 6.0.1 Release及以上版本。
