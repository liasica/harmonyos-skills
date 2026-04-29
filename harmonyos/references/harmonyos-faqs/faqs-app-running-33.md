---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-33
title: 启动模拟器，提示镜像文件缺失
breadcrumb: FAQ > DevEco Studio > 应用运行 > 启动模拟器，提示镜像文件缺失
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:18+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:4a4610b89aafd791bd5728922e76048eba72d4b053f22916aca09e2c310cf9b7
---

**问题现象**

启动模拟器失败，提示“system-image文件缺失”或“The system-image file is missing.”，原因是模拟器镜像文件缺失。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/-pKQcZSlSweZZZvnmZrxQg/zh-cn_image_0000002229758805.png?HW-CC-KV=V1&HW-CC-Date=20260429T062117Z&HW-CC-Expire=86400&HW-CC-Sign=F0230773D47379DCC8B89E2317746C5A71699831ED0BC4992FB08187849476DA "点击放大")

**解决措施**

请通过以下两种方式解决：

* 单击菜单栏的Tools > Device Manager。在Local Emulator页签，单击右下角的New Emulator按钮。在虚拟设备配置界面，更新模拟器的镜像。
* 删除已创建的模拟器，然后重新创建。
