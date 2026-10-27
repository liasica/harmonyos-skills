---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-118
title: 编译报错“The path XX is not writable. please choose a new location”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The path XX is not writable. please choose a new location”
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:54+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:cfe165f054df58ee9214bf37c7c96e19c0541ffdd241854754d86286437d5643
---

**问题现象**

在Mac上，通过打开DMG文件中的DevEco Studio图标启动DevEco Studio时，如果构建报错“The path XX is not writable. please choose a new location”，请选择一个新的位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/BpvSfaMbTmGmhWlFH6VnAg/zh-cn_image_0000002654837911.png)

**问题原因**

在Mac上直接通过DMG中的DevEco Studio图标打开DevEco Studio，会以只读方式打开。内置在DevEco Studio中的文件没有写权限。

**解决措施**

将“DevEco-Studio.app”拖拽到“Applications”文件夹中，安装后再使用。
