---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-run-device
title: 使用本地真机运行应用
breadcrumb: 指南 > 编写与调试应用 > 使用本地真机运行应用
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:24+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:173c310bfcd01123fc5187737376a97f853d666fe0aa93be9b1a512488d027bd
---

在本地真机中运行HarmonyOS应用/元服务，可以采用USB连接方式或者无线连接方式。

**说明** 

Wearable设备仅支持无线连接方式（Lite Wearable设备不支持）。

## 前提条件

* 确保设备系统版本升级到[HarmonyOS NEXT Developer Beta1](../harmonyos-releases/overview-500.md#section849861583816)或以上。
* 在真机设备上查看**设置 > 系统**中开发者选项是否存在，如果不存在，可在**设置 > *具体的设备名称***中，连续七次单击**软件版本**，直到提示“开启开发者选项”，点击**确认开启**后输入PIN码（如果已设置），设备将自动重启，请等待设备完成重启。
* 在设备运行应用/元服务需要根据[配置调试签名](ide-signing.md)章节，提前对应用/元服务进行签名。

## 使用USB连接方式

1. 使用USB方式，将真机设备与PC端进行连接。
2. 在**设置 > 系统 > 开发者选项**中，打开**USB调试**开关（确保设备已连接USB）。
3. 在真机设备中会弹出“允许USB调试”的弹框，单击**允许**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/LHm7klPmT-q_NrRuOYtK1g/zh-cn_image_0000002701823842.png)
4. 在菜单栏中，单击**Run>Run'模块名称'**或![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/16LBCCoDSpCGZsA0EsbonA/zh-cn_image_0000002731383141.png)，或使用默认快捷键**Shift+F10**（macOS为**Control+R**）运行应用/元服务。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/ZQv3P9LfSIClgPxIiONOMA/zh-cn_image_0000002731543121.png)
5. DevEco Studio启动HAP的编译构建和安装。安装成功后，设备会自动运行安装的HarmonyOS应用/元服务。

### 使用设备连接助手排查问题

从DevEco Studio 5.1.1 Beta1版本开始，设备连接后，如果DevEco Studio无法识别到设备，显示“No Devices”，可使用设备连接助手来排查问题。点击设备下拉框，并点击**Troubleshoot Device Connections**打开该功能，分为三个步骤，每个步骤排查完后点击**Next**排查下一个。

1. **通过USB连接设备：**根据界面提示，使用USB连接设备后，点击**Rescan Devices**按钮，扫描已连接的设备，确保扫描结果中包含待调试的设备。
2. **启用USB调试：**根据界面提示，确保设备系统版本正确，并且启用开发者选项和USB调试。
3. **重启HDC服务：**如果DevEco Studio仍然无法识别设备，点击**Restart hdc Service**按钮重启HDC服务，重启后HDC会重新识别设备。如果重启后仍识别不到设备，请参考[设备连接后，无法识别设备的处理指导](../harmonyos-faqs/faqs-app-debugging-3.md)或[如何解决设备无法识别问题](../harmonyos-faqs/faqs-performance-analysis-kit-32.md)。

## 使用无线连接方式

1. 将真机设备和PC连接到同一WLAN网络。
2. 在**设置 > 系统 >** **开发者选项**中，打开**无线调试**或**通过WLAN调试**（Wearable设备）开关，并获取设备端的IP地址和端口号。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/HoILQ95mToGjyzYCs82Ouw/zh-cn_image_0000002731543119.png "点击放大")
3. 连接设备，有两种方式。
   * 通过DevEco Studio连接。
     + **6.1.1 Release（6.1.1.300）及以上版本：**单击菜单栏**Tools > IP Connection**，或者在设备下拉列表单击**IP Connection**，按照IP:port格式输入设备的IP地址和端口号，单击**Connect**连接设备，连接成功后会显示在列表中，默认开启屏幕常亮。

       开启屏幕常亮后，DevEco Studio会持续向设备发送亮屏指令，使设备屏幕常亮。即使手动将设备锁屏，屏幕也会自动亮起，这是DevEco Studio为保持屏幕常亮而发送亮屏指令的正常行为。

       如需退出屏幕常亮，有以下方式：

       - 方式一：在IP Connection面板中单击**Disable Screen Always-On**。
       - 方式二：断开设备连接。

       退出后，DevEco Studio将停止发送亮屏指令，设备可正常进入休眠。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/im93NIUNR3y4n4yxDaKsVQ/zh-cn_image_0000002701663924.png)
     + **6.1.1 Release（6.1.1.300）以下版本：**单击菜单栏**Tools > IP Connection**，输入连接设备的IP地址和端口号，单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/L01NCQFWRWusYR9ylEn-pw/zh-cn_image_0000002701663918.png)，连接正常后，设备状态为**online**。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/MmlhBrxsQY-UyknAMnClQQ/zh-cn_image_0000002731543115.png)
   * 通过hdc连接，关于hdc工具的使用指导请参考[hdc](hdc.md)。

     ```bash
     hdc tconn 设备IP地址:端口号
     ```
4. 在菜单栏中，单击**Run>Run'模块名称'**或![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/79WA9BS8QlaUQUYsK0dyvg/zh-cn_image_0000002701663920.png)，或使用默认快捷键**Shift+F10**（macOS为**Control+R**）运行应用/元服务。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/NnPRyVsLQniBkx5XLqu1MA/zh-cn_image_0000002731383143.png)
5. DevEco Studio启动HAP的编译构建和安装。安装成功后，设备会自动运行安装的HarmonyOS应用/元服务。
