---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-run-device
title: 使用本地真机运行应用
breadcrumb: 指南 > 编写与调试应用 > 使用本地真机运行应用
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7514dfd8cca409f6801aeb007c53edd12a0fdebd05d024c62498ca1884bda66d
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/LQJ20k0CTeKpDNHhKL1_vw/zh-cn_image_0000002530753700.png?HW-CC-KV=V1&HW-CC-Date=20260427T235638Z&HW-CC-Expire=86400&HW-CC-Sign=D5762D2F60B6CF057CD621DCA57FC1422BE4EFE717ADEB06107E51F05DD7BC1C)
4. 在菜单栏中，单击**Run>Run'模块名称'**或![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/KM6MQpDIQGiVddvyWbsPeQ/zh-cn_image_0000002561753635.png?HW-CC-KV=V1&HW-CC-Date=20260427T235638Z&HW-CC-Expire=86400&HW-CC-Sign=CEE972FFDD1D594B9096B15B231445B1D8F9429158935C65C3B53516260BAAC1)，或使用默认快捷键**Shift+F10**（macOS为**Control+R**）运行应用/元服务。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/Y9Rol6Y7ScuurlVzTevfvg/zh-cn_image_0000002561753637.png?HW-CC-KV=V1&HW-CC-Date=20260427T235638Z&HW-CC-Expire=86400&HW-CC-Sign=8F766E5F3CFDAA180461BD6389B10FC7375A6C9FF44E9386CA094C443419ECC1)
5. DevEco Studio启动HAP的编译构建和安装。安装成功后，设备会自动运行安装的HarmonyOS应用/元服务。

### 使用设备连接助手排查问题

从DevEco Studio 5.1.1 Beta1版本开始，设备连接后，如果DevEco Studio无法识别到设备，显示“No Devices”，可使用设备连接助手来排查问题。点击设备下拉框，并点击**Troubleshoot Device Connections**打开该功能，分为三个步骤，每个步骤排查完后点击**Next**排查下一个。

1. **通过USB连接设备：**根据界面提示，使用USB连接设备后，点击**Rescan Devices**按钮，扫描已连接的设备，确保扫描结果中包含待调试的设备。
2. **启用USB调试：**根据界面提示，确保设备系统版本正确，并且启用开发者选项和USB调试。
3. **重启HDC服务：**如果DevEco Studio仍然无法识别设备，点击**Restart hdc Service**按钮重启HDC服务，重启后HDC会重新识别设备。如果重启后仍识别不到设备，请参考[设备连接后，无法识别设备的处理指导](../harmonyos-faqs/faqs-app-debugging-3.md)或[如何解决设备无法识别问题](../harmonyos-faqs/faqs-performance-analysis-kit-32.md)。

## 使用无线连接方式

1. 将真机设备和PC连接到同一WLAN网络。
2. 在**设置 > 系统 >** **开发者选项**中，打开**无线调试**或**通过WLAN调试**（Wearable设备）开关，并获取设备端的IP地址和端口号。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/bkW4KVWLQxC0x7vfrpPPuw/zh-cn_image_0000002530753696.png?HW-CC-KV=V1&HW-CC-Date=20260427T235638Z&HW-CC-Expire=86400&HW-CC-Sign=5C209929091EDB0C3CE4797CBBF74B61C6D128BBE1F32D21FCE4347AD7541470 "点击放大")
3. 连接设备，有两种方式。
   * 在DevEco Studio菜单栏中，单击**Tools > IP Connection**，输入连接设备的IP地址和端口号，单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/1VLHx9WoSCW8YUBsN3BvDw/zh-cn_image_0000002561833605.png?HW-CC-KV=V1&HW-CC-Date=20260427T235638Z&HW-CC-Expire=86400&HW-CC-Sign=E6E6AF22F5D1A147F452D91C31CACFFABB738CC438C13856C933608509B3EFA8)，连接正常后，设备状态为**online**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/wbkGncctS_qFjNV5Vckugg/zh-cn_image_0000002561753629.png?HW-CC-KV=V1&HW-CC-Date=20260427T235638Z&HW-CC-Expire=86400&HW-CC-Sign=0A562B8A31454B5A94A59ADD430BFD1C91AA09526629D7F54BE95407CBBC8C58)
   * 执行hdc命令，关于hdc工具的使用指导请参考[hdc](hdc.md)。

     ```
     1. hdc tconn 设备IP地址:端口号
     ```
4. 在菜单栏中，单击**Run>Run'模块名称'**或![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/Gq8Ach0eQ72m6PRA1M9kmQ/zh-cn_image_0000002530913684.png?HW-CC-KV=V1&HW-CC-Date=20260427T235638Z&HW-CC-Expire=86400&HW-CC-Sign=C8345F6ACAD4DFC00AB7F4A37629BA47A8E0E5A54E2AD57EA21DD02AC1222B3F)，或使用默认快捷键**Shift+F10**（macOS为**Control+R**）运行应用/元服务。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/vbrRbj2FRiyL5FO3JG-rVw/zh-cn_image_0000002530753694.png?HW-CC-KV=V1&HW-CC-Date=20260427T235638Z&HW-CC-Expire=86400&HW-CC-Sign=5A8810DB164E2A7D07E203FE9EE8BC17AF622B241D81D338799824C8E7CFF116)
5. DevEco Studio启动HAP的编译构建和安装。安装成功后，设备会自动运行安装的HarmonyOS应用/元服务。
