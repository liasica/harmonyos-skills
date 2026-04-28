---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-118
title: 编译报错“The path XX is not writable. please choose a new location”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The path XX is not writable. please choose a new location”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:32+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:305756e2515d7cce4a4a494f0deb85fff46b106008b3e092c0d1935f37928a84
---

**问题现象**

在Mac上，通过打开DMG文件中的DevEco Studio图标启动DevEco Studio时，如果构建报错“The path XX is not writable. please choose a new location”，请选择一个新的位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/g2YlPHR7SrunzWHIMCAaAg/zh-cn_image_0000002229604193.png?HW-CC-KV=V1&HW-CC-Date=20260428T002931Z&HW-CC-Expire=86400&HW-CC-Sign=F8DF2D2E35632C105FC5DEAAF5FCC2DDD38AF50B83422F1CCB42627B88AD95E1)

**问题原因**

在Mac上直接通过DMG中的DevEco Studio图标打开DevEco Studio，会以只读方式打开。内置在DevEco Studio中的文件没有写权限。

**解决措施**

将“DevEco-Studio.app”拖拽到“Applications”文件夹中，安装后再使用。
