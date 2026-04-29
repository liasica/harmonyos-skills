---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-35
title: DevEco Studio安装HAP时报错“FileTransfer Failed: Error while Deploy Hap”
breadcrumb: FAQ > DevEco Studio > 应用调试 > DevEco Studio安装HAP时报错“FileTransfer Failed: Error while Deploy Hap”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:26+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d53a34f6f0fda643a4c1bfc22336cbd9992d82d396d613050b2395af2b6bf68f
---

**问题现象**

DevEco Studio安装HAP时报错“FileTransfer Failed: Error while Deploy Hap”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/myB6FhdNSWOgSRGLv8s4hw/zh-cn_image_0000002215508376.png?HW-CC-KV=V1&HW-CC-Date=20260429T062125Z&HW-CC-Expire=86400&HW-CC-Sign=9E29F54476844C4FA5A6360AC0D2BCEABFB3435F4F7A78505B9C2BBAA74A6D81)

**解决措施**

使用真机场景：请更换数据线或PC侧USB接口后尝试。

使用模拟器场景：

* 在Local Emulator的设备列表窗口，点击“Wipe User Data”清除数据，启动模拟器并重新运行工程。
* 打开命令行工具，并进入DevEco Studio安装目录下的sdk\default\openharmony\toolchains路径，执行 hdc kill -r 命令，启动模拟器，重新运行工程。
