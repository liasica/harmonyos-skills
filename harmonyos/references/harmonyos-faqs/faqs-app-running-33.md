---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-33
title: 启动模拟器，提示镜像文件缺失
breadcrumb: FAQ > DevEco Studio > 应用运行 > 启动模拟器，提示镜像文件缺失
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:56+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:789f68ea40b8229575c920dcf7567f09e8893a925c655d308f8d9237d5de5604
---

**问题现象**

启动模拟器失败，提示“system-image文件缺失”或“The system-image file is missing.”，原因是模拟器镜像文件缺失。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/hrUxNmAhSNa6cfKsv0Zzsw/zh-cn_image_0000002624478764.png "点击放大")

**解决措施**

请通过以下两种方式解决：

* 单击菜单栏的Tools > Device Manager。在Local Emulator页签，单击右下角的New Emulator按钮。在虚拟设备配置界面，更新模拟器的镜像。
* 删除已创建的模拟器，然后重新创建。
