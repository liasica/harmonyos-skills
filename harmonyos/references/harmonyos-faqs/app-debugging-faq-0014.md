---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/app-debugging-faq-0014
title: DevEco Studio安装HAP报错FileTransfer Failed问题排查
breadcrumb: FAQ > DevEco Studio > 应用调试 > 常见问题 > DevEco Studio安装HAP报错FileTransfer Failed问题排查
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:59+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:788eddc563441d8603020f716260253f98fd3d8b7e350913afd1fbc881e02066
---

**Q：DevEco Studio安装HAP时报错“FileTransfer Failed: Error while Deploy Hap”如何解决？**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/tKgLBagZQzaYeqOsFWTfwA/zh-cn_image_0000002803181263.png "点击放大")

**A**：

使用真机场景：请更换数据线或PC侧USB接口后尝试。

使用模拟器场景：

* 在Local Emulator的设备列表窗口，点击“Wipe User Data”清除数据，启动模拟器并重新运行工程。
* 打开命令行工具，并进入DevEco Studio安装目录下的sdk\default\openharmony\toolchains路径，执行 hdc kill -r 命令，启动模拟器，重新运行工程。
