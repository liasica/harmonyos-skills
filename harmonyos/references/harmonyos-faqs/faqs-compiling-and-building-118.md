---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-118
title: 编译报错“The path XX is not writable. please choose a new location”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The path XX is not writable. please choose a new location”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:45+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5ef9bfcbfc31d2da204dabf6d9baaf040a737e5d1180f5b3d23311e7857090b7
---

**问题现象**

在Mac上，通过打开DMG文件中的DevEco Studio图标启动DevEco Studio时，如果构建报错“The path XX is not writable. please choose a new location”，请选择一个新的位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/g2YlPHR7SrunzWHIMCAaAg/zh-cn_image_0000002229604193.png?HW-CC-KV=V1&HW-CC-Date=20260429T062044Z&HW-CC-Expire=86400&HW-CC-Sign=AECA4AAD4CFF704C0A25BA8742578B97318FBDB9934A469DC9FD8F9824DAEDC3)

**问题原因**

在Mac上直接通过DMG中的DevEco Studio图标打开DevEco Studio，会以只读方式打开。内置在DevEco Studio中的文件没有写权限。

**解决措施**

将“DevEco-Studio.app”拖拽到“Applications”文件夹中，安装后再使用。
