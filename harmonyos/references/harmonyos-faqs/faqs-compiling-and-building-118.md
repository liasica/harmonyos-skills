---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-118
title: 编译报错“The path XX is not writable. please choose a new location”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The path XX is not writable. please choose a new location”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:45+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b8eacf74de4c8e8242e6f6fd4b84870f11c577f37330c4ebeaa1320f3c8b5c1e
---

**问题现象**

在Mac上，通过打开DMG文件中的DevEco Studio图标启动DevEco Studio时，如果构建报错“The path XX is not writable. please choose a new location”，请选择一个新的位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/g2YlPHR7SrunzWHIMCAaAg/zh-cn_image_0000002229604193.png)

**问题原因**

在Mac上直接通过DMG中的DevEco Studio图标打开DevEco Studio，会以只读方式打开。内置在DevEco Studio中的文件没有写权限。

**解决措施**

将“DevEco-Studio.app”拖拽到“Applications”文件夹中，安装后再使用。
