---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-run-device
title: 使用本地真机运行应用
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 使用本地真机运行应用
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:20+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:8f231bd74b0c06878328bd9edf1781d3fe7729146c86cbfc1c75c329adb8a674
---

鸿蒙电脑DevEco Studio允许开发者连接本地真机运行HarmonyOS应用/元服务，可以采用USB连接方式。

## 前提条件

* 在真机设备上查看**设置** **> 系统**中**开发者选项**是否存在，如果不存在，可在**设置 > *具体的设备名称***中，连续七次单击**软件****版本**，直到提示“开启开发者选项”，点击**确认开启**后输入PIN码（如果已设置），设备将自动重启，请等待设备完成重启。
* 2in1设备需要确保关闭反向超级快充模式，在该模式下不支持通过USB调试设备。在2in1设备的通知中心查看提示并关闭。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/hnD9VlryT4i7ISzrJ0EajQ/zh-cn_image_0000002750169646.png)
* 在设备运行应用/元服务需要根据[配置调试签名](ide-hmos-signing.md)章节，提前对应用/元服务进行签名。

## 使用USB连接方式

1. 使用USB方式，将真机设备与2in1设备进行连接。
2. 在**设置 > 系统 > 开发者选项**中，打开**USB调试**开关（确保设备已连接USB）。
3. 在真机设备中会弹出“允许USB调试”的弹框，单击**允许**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/Z3wgaHhESUaWiuhF-O9uWA/zh-cn_image_0000002779728821.png)
4. 在界面上方选择模块后，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/4J-CyIrlQAWOu3BazK81KQ/zh-cn_image_0000002750169648.png)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/KBD_sYWdTnObdlEOOiW7gg/zh-cn_image_0000002779608671.png)
5. DevEco Studio启动HAP的编译构建和安装。安装成功后，设备会自动运行安装的HarmonyOS应用/元服务。

**说明** 

如果DevEco Studio无法识别到已连接的设备，可参考[设备连接后，无法识别设备的处理指导](../harmonyos-faqs/faqs-app-debugging-3.md)。
