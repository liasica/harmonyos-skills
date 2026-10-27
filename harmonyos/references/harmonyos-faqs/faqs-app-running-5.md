---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-5
title: 运行工程到本地模拟器，提示“Failed to get the device apiVersion”
breadcrumb: FAQ > DevEco Studio > 应用运行 > 运行工程到本地模拟器，提示“Failed to get the device apiVersion”
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:58+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:fd7ee7778c3c008441a479779bf8227d1cca9320d931c5d76e563e15542ac059
---

**问题现象**

本地模拟器启动后，运行工程到模拟器，提示“Failed to get the device apiVersion”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/BwR9O1NtT32WIrTO4GL7iQ/zh-cn_image_0000002654798111.png)

**解决措施**

可以通过以下方法重新运行工程：

* 在**Local Emulator**的设备列表窗口，点击“Wipe User Data”清除模拟器数据，然后重新启动模拟器并运行工程。
* 打开命令行工具，进入HarmonyOS SDK安装目录下的 `default/base/toolchains` 路径，执行以下命令重启 hdc server：

  ```powershell
  ./hdc kill -r
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/BLdV_VsDQ7exSsHT_e2pDA/zh-cn_image_0000002624638658.png)
