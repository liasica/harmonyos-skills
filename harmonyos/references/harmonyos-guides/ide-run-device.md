---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-run-device
title: 使用本地真机运行应用
breadcrumb: 指南 > 编写与调试应用 > 使用本地真机运行应用
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2fe856912b788e1762d93f79f3b8cac76aca612a957bcf51bea2c56a87ad8852
---

在本地真机中运行HarmonyOS应用/元服务，可以采用USB连接方式或者无线连接方式。

说明

Wearable设备仅支持无线连接方式（Lite Wearable设备不支持）。

## 前提条件

* 确保设备系统版本升级到[HarmonyOS NEXT Developer Beta1](../harmonyos-releases/overview-500.md#section849861583816)或以上。
* 在真机设备上查看**设置 > 系统**中开发者选项是否存在，如果不存在，可在**设置 > *具体的设备名称***中，连续七次单击**软件版本**，直到提示“开启开发者选项”，点击**确认开启**后输入PIN码（如果已设置），设备将自动重启，请等待设备完成重启。
* 在设备运行应用/元服务需要根据[配置调试签名](ide-signing.md)章节，提前对应用/元服务进行签名。

## 使用USB连接方式

1. 使用USB方式，将真机设备与PC端进行连接。
2. 在**设置 > 系统 > 开发者选项**中，打开**USB调试**开关（确保设备已连接USB）。
3. 在真机设备中会弹出“允许USB调试”的弹框，单击**允许**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/Oyuug85pRguiANctBfqTLw/zh-cn_image_0000002530753700.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=087974E739C5F0BE7C7640E55C20FAE694E5879DA673B04068CF4B8F3C317908)
4. 在菜单栏中，单击**Run>Run'模块名称'**或![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/HA9pSB-1RsW5uicC0euiag/zh-cn_image_0000002561753635.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=CB9AE50015EBE29F951EFD40AEDE8CDAA456A51554997D1E95654084B86C5234)，或使用默认快捷键**Shift+F10**（macOS为**Control+R**）运行应用/元服务。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/t8EbChjsRweUbEsRt0FOhQ/zh-cn_image_0000002561753637.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=8BE0E4DF9C257593EDD1609D52AA2BC66689866ADBBD83EC332ADE130D98B966)
5. DevEco Studio启动HAP的编译构建和安装。安装成功后，设备会自动运行安装的HarmonyOS应用/元服务。

### 使用设备连接助手排查问题

从DevEco Studio 5.1.1 Beta1版本开始，设备连接后，如果DevEco Studio无法识别到设备，显示“No Devices”，可使用设备连接助手来排查问题。点击设备下拉框，并点击**Troubleshoot Device Connections**打开该功能，分为三个步骤，每个步骤排查完后点击**Next**排查下一个。

1. **通过USB连接设备：**根据界面提示，使用USB连接设备后，点击**Rescan Devices**按钮，扫描已连接的设备，确保扫描结果中包含待调试的设备。
2. **启用USB调试：**根据界面提示，确保设备系统版本正确，并且启用开发者选项和USB调试。
3. **重启HDC服务：**如果DevEco Studio仍然无法识别设备，点击**Restart hdc Service**按钮重启HDC服务，重启后HDC会重新识别设备。如果重启后仍识别不到设备，请参考[设备连接后，无法识别设备的处理指导](../harmonyos-faqs/faqs-app-debugging-3.md)或[如何解决设备无法识别问题](../harmonyos-faqs/faqs-performance-analysis-kit-32.md)。

## 使用无线连接方式

1. 将真机设备和PC连接到同一WLAN网络。
2. 在**设置 > 系统 >** **开发者选项**中，打开**无线调试**或**通过WLAN调试**（Wearable设备）开关，并获取设备端的IP地址和端口号。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/BJkPgitLTcW1zFJuQI3sHQ/zh-cn_image_0000002530753696.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=AC4D90B6934B4866F9173719945A4DCBEC87EA0D28741111B878D662641D081A "点击放大")
3. 连接设备，有两种方式。
   * 在DevEco Studio菜单栏中，单击**Tools > IP Connection**，输入连接设备的IP地址和端口号，单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/Dk2E8d71Svizmui5_epUog/zh-cn_image_0000002561833605.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=08E94CEE74559FBD66C270F9AF67F1EBD0C02788D2884BC546984505D503C0AE)，连接正常后，设备状态为**online**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/RO1kecHUSHyo-R0jIvFm-Q/zh-cn_image_0000002561753629.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=E576647C248772777A04929D57B71F4E48F590E29D083D2F641C351EDCC8F7EA)
   * 执行hdc命令，关于hdc工具的使用指导请参考[hdc](hdc.md)。

     ```
     1. hdc tconn 设备IP地址:端口号
     ```
4. 在菜单栏中，单击**Run>Run'模块名称'**或![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/7nJF-G6ARie-FcxQloQAgw/zh-cn_image_0000002530913684.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=3424A6FEAACF83AA6938032971C2A7B75B47FC21E078C997702F768882B087FB)，或使用默认快捷键**Shift+F10**（macOS为**Control+R**）运行应用/元服务。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/oPhV_4ezTSOLT46o6l2nPg/zh-cn_image_0000002530753694.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=4F3BD10C6B6F2076A1A6BD0FA6E06E5960A937D4A965DBAC4361F37832306058)
5. DevEco Studio启动HAP的编译构建和安装。安装成功后，设备会自动运行安装的HarmonyOS应用/元服务。
