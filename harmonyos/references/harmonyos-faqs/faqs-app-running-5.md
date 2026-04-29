---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-5
title: 运行工程到本地模拟器，提示“Failed to get the device apiVersion”
breadcrumb: FAQ > DevEco Studio > 应用运行 > 运行工程到本地模拟器，提示“Failed to get the device apiVersion”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:12+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f9f7099c1184b40713198ae633f6d6ae300cc7b360fd947f716e03ed59ab8ac5
---

**问题现象**

本地模拟器启动后，运行工程到模拟器，提示“Failed to get the device apiVersion”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/kc43G3pfTRGbhcgMgufe4Q/zh-cn_image_0000002194317932.png?HW-CC-KV=V1&HW-CC-Date=20260429T062111Z&HW-CC-Expire=86400&HW-CC-Sign=B8B364EB59496BE946D068AB43E4FE6E33E06EE7823CE5B1F971DAAD8A1A510D)

**解决措施**

可以通过以下方法重新运行工程：

* 在**Local Emulator**的设备列表窗口，点击“Wipe User Data”清除模拟器数据，然后重新启动模拟器并运行工程。
* 打开命令行工具，进入HarmonyOS SDK安装目录下的 `default/base/toolchains` 路径，执行以下命令重启 hdc server：

  ```
  1. ./hdc kill -r
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/9vDwYwvFR5qIntKHPE3Pug/zh-cn_image_0000002229758185.png?HW-CC-KV=V1&HW-CC-Date=20260429T062111Z&HW-CC-Expire=86400&HW-CC-Sign=ECBE848D841143D2C815BA67AEF33ED1B54F4E707A879323A3C2F2419C49821A)
