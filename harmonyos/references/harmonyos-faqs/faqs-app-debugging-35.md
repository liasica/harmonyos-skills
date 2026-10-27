---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-35
title: "DevEco Studio安装HAP时报错“FileTransfer Failed: Error while Deploy Hap”"
breadcrumb: "FAQ > DevEco Studio > 应用调试 > DevEco Studio安装HAP时报错“FileTransfer Failed: Error while Deploy Hap”"
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:59+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:ef8d56eb79cfad1c43f632cd6bb9449e74c98d3c1412f62779744e6ecbaad9a9
---

**问题现象**

DevEco Studio安装HAP时报错“FileTransfer Failed: Error while Deploy Hap”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/2PEaUO2ZSPqxFWlg1T9hcQ/zh-cn_image_0000002654798167.png)

**解决措施**

使用真机场景：请更换数据线或PC侧USB接口后尝试。

使用模拟器场景：

* 在Local Emulator的设备列表窗口，点击“Wipe User Data”清除数据，启动模拟器并重新运行工程。
* 打开命令行工具，并进入DevEco Studio安装目录下的sdk\default\openharmony\toolchains路径，执行 hdc kill -r 命令，启动模拟器，重新运行工程。
