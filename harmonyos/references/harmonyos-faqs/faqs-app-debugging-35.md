---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-35
title: DevEco Studio安装HAP时报错“FileTransfer Failed: Error while Deploy Hap”
breadcrumb: FAQ > DevEco Studio > 应用调试 > DevEco Studio安装HAP时报错“FileTransfer Failed: Error while Deploy Hap”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:10+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c330c900a860bdf56df645e818fdaf543393686c2fbe4a2ce07a356a9da70602
---

**问题现象**

DevEco Studio安装HAP时报错“FileTransfer Failed: Error while Deploy Hap”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/myB6FhdNSWOgSRGLv8s4hw/zh-cn_image_0000002215508376.png?HW-CC-KV=V1&HW-CC-Date=20260428T003009Z&HW-CC-Expire=86400&HW-CC-Sign=BF5F62A06ED9665112BE9EB4E112270600FBF9CCD882B1F0A9E4A5EB9ED6912D)

**解决措施**

使用真机场景：请更换数据线或PC侧USB接口后尝试。

使用模拟器场景：

* 在Local Emulator的设备列表窗口，点击“Wipe User Data”清除数据，启动模拟器并重新运行工程。
* 打开命令行工具，并进入DevEco Studio安装目录下的sdk\default\openharmony\toolchains路径，执行 hdc kill -r 命令，启动模拟器，重新运行工程。
