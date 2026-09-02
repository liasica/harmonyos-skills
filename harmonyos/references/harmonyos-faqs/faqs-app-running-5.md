---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-5
title: 运行工程到本地模拟器，提示“Failed to get the device apiVersion”
breadcrumb: FAQ > DevEco Studio > 应用运行 > 运行工程到本地模拟器，提示“Failed to get the device apiVersion”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:12+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:99b154dd05bb49eabf5794d37627384bb5ba13a79c3274afb0143429ec6880e2
---

**问题现象**

本地模拟器启动后，运行工程到模拟器，提示“Failed to get the device apiVersion”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/kc43G3pfTRGbhcgMgufe4Q/zh-cn_image_0000002194317932.png)

**解决措施**

可以通过以下方法重新运行工程：

* 在**Local Emulator**的设备列表窗口，点击“Wipe User Data”清除模拟器数据，然后重新启动模拟器并运行工程。
* 打开命令行工具，进入HarmonyOS SDK安装目录下的 `default/base/toolchains` 路径，执行以下命令重启 hdc server：

  ```
  1. ./hdc kill -r
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/9vDwYwvFR5qIntKHPE3Pug/zh-cn_image_0000002229758185.png)
