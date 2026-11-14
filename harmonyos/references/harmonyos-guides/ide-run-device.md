---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-run-device
title: 使用本地真机运行应用
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 使用本地真机运行应用
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:58+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:070ffd3400d8a8dc88ec88ddcb2b3416211e33ffe9dd66d211a36d3e42ed36f8
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/8bms-2uzTUCnt4N65_g3qQ/zh-cn_image_0000002808887023.png?HW-CC-KV=V1&HW-CC-Date=20261114T004711Z&HW-CC-Expire=31536000000&HW-CC-Sign=0F7C9A2AB45D5D5056DADCBE7A6C879FA06E8D25C7C47D89B62F6C9AA93F26DC)
4. 在菜单栏中，单击**Run>Run '模块名称'**或![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/JlH6oDyrSWm8OHvukIEVbg/zh-cn_image_0000002808766941.png?HW-CC-KV=V1&HW-CC-Date=20261114T004711Z&HW-CC-Expire=31536000000&HW-CC-Sign=1351F136811093D6EF49DC6317CD04AC066D2B1070DCB49538FE923E22BA3901)，或使用默认快捷键**Shift+F10**（macOS为**Control+R**）运行应用/元服务。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/Mbb3I7tbRzaMFjg4VQxyow/zh-cn_image_0000002779567370.png?HW-CC-KV=V1&HW-CC-Date=20261114T004711Z&HW-CC-Expire=31536000000&HW-CC-Sign=C2CF8765FC7D6FB4CB1A16DFF78A17FFF607C887BF9D59C77ACEF187119356A7)
5. DevEco Studio启动HAP的编译构建和安装。安装成功后，设备会自动运行安装的HarmonyOS应用/元服务。

### 使用设备连接助手排查问题

从DevEco Studio 5.1.1 Beta1版本开始，设备连接后，如果DevEco Studio无法识别到设备，显示**No Devices**或**No Available Devices**，可使用设备连接助手来排查问题。

**DevEco Studio 6.1.1 Release及以上版本**

单击运行或调试按钮可直接打开设备连接助手，也可以单击设备下拉框，并单击**Troubleshoot Device Connections**打开该功能。

开发者可以查看到设备的状态，根据界面提示初步排查问题，也可以尝试单击**Restart hdc**重启hdc服务，重新识别设备。

如果重启后仍识别不到设备，请参考[真机设备识别常见问题](../harmonyos-faqs/app-debugging-faq-0012.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/rV3P38ncQsKuAgXmwwjuDA/zh-cn_image_0000002779567368.png?HW-CC-KV=V1&HW-CC-Date=20261114T004711Z&HW-CC-Expire=31536000000&HW-CC-Sign=830933E5AFB3B8C6674C9C8E6A90C881B70F612ADC37B7AFB96168A0D2E4D446)

**DevEco Studio 6.1.1 Release****以下版本**

单击设备下拉框，并单击**Troubleshoot Device Connections**打开该功能，分为三个步骤，每个步骤排查完后单击**Next**排查下一个。

1. **通过USB连接设备：**根据界面提示，使用USB连接设备后，点击**Rescan Devices**按钮，扫描已连接的设备，确保扫描结果中包含待调试的设备。
2. **启用USB调试：**根据界面提示，确保设备系统版本正确，并且启用开发者选项和USB调试。
3. **重启hdc服务：**如果DevEco Studio仍然无法识别设备，单击**Restart hdc Service**按钮重启hdc服务，重启后hdc会重新识别设备。如果重启后仍识别不到设备，请参考[真机设备识别常见问题](../harmonyos-faqs/app-debugging-faq-0012.md)。

## 使用无线连接方式

1. 将真机设备和PC连接到同一WLAN网络。
2. 在**设置 > 系统 >** **开发者选项**中，打开**无线调试**或**通过WLAN调试**（Wearable设备）开关，并获取设备端的IP地址和端口号。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/6i8ZQPvWTXixZMVd023yNQ/zh-cn_image_0000002779567366.png?HW-CC-KV=V1&HW-CC-Date=20261114T004711Z&HW-CC-Expire=31536000000&HW-CC-Sign=38D8B76016077E64DC3CB692FF7108399F8431589C50713778E87AF80A093017 "点击放大")
3. 连接设备，有两种方式。
   * 通过DevEco Studio连接。
     + **6.1.1 Release及以上版本：**单击菜单栏**Tools > IP Connection**，或者在设备下拉列表单击**IP Connection**，按照IP:port格式输入设备的IP地址和端口号，单击**Connect**连接设备，连接成功后会显示在列表中，默认开启屏幕常亮。

       开启屏幕常亮后，DevEco Studio会持续向设备发送亮屏指令，使设备屏幕常亮。即使手动将设备锁屏，屏幕也会自动亮起，这是DevEco Studio为保持屏幕常亮而发送亮屏指令的正常行为。

       如需退出屏幕常亮，有以下方式：

       - 方式一：在IP Connection面板中单击**Disable Screen Always-On**。
       - 方式二：断开设备连接。

       退出后，DevEco Studio将停止发送亮屏指令，设备可正常进入休眠。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/adQQuDLLRo6djkt8CVj41A/zh-cn_image_0000002779407388.png?HW-CC-KV=V1&HW-CC-Date=20261114T004711Z&HW-CC-Expire=31536000000&HW-CC-Sign=A797C108ADD841C55C6155CBA0C9D155696926B70AE7110C4DF5BA3292664C56)
     + **6.1.1 Release以下版本：**单击菜单栏**Tools > IP Connection**，输入连接设备的IP地址和端口号，单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/-ONBxwFDSSCUTY_xZ0Plhw/zh-cn_image_0000002808887021.png?HW-CC-KV=V1&HW-CC-Date=20261114T004711Z&HW-CC-Expire=31536000000&HW-CC-Sign=8D0D6B8B9223301ED2253199CF0D369285E83F204B000360AE1BF107D410155F)，连接正常后，设备状态为**online**。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/-Ab5ulCYTN6khcJT7hfTEg/zh-cn_image_0000002808766943.png?HW-CC-KV=V1&HW-CC-Date=20261114T004711Z&HW-CC-Expire=31536000000&HW-CC-Sign=AD871C0FAAACA487654BC1A4BDFFA00AB01A594896484FBF2848C93277B4011B)
   * 通过hdc连接，关于hdc工具的使用指导请参考[hdc](hdc.md)。

     ```bash
     hdc tconn 设备IP地址:端口号
     ```
4. 在菜单栏中，单击**Run>Run'模块名称'**或![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/pkHcZ4N9RjewKVcmAao7wQ/zh-cn_image_0000002808887025.png?HW-CC-KV=V1&HW-CC-Date=20261114T004711Z&HW-CC-Expire=31536000000&HW-CC-Sign=6B313E65F26D1A1E7CFFF261520E368DF91D8189BF53F3549097B79F6DC36FCC)，或使用默认快捷键**Shift+F10**（macOS为**Control+R**）运行应用/元服务。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/2S6mvFkxTzyGLRJN9nv6Bg/zh-cn_image_0000002808766945.png?HW-CC-KV=V1&HW-CC-Date=20261114T004711Z&HW-CC-Expire=31536000000&HW-CC-Sign=6863B2B43E8973B166FD8A6DB691CA2C165C49A5D9A091D0BB685294F42AF1CF)
5. DevEco Studio启动HAP的编译构建和安装。安装成功后，设备会自动运行安装的HarmonyOS应用/元服务。

### 使用Wearable设备运行Lite Wearable应用

从26.0.1版本开始，DevEco Studio支持将Lite Wearable应用推包到支持双模式（全能模式和省电模式，在**设置 > 双模式管理**中查看）的Wearable设备上运行，但不支持调试。

在Wearable设备上运行时，仅支持手动签名。在获取签名需要的调试Profile时，可通过命令hdc shell hidumper -s 4606 -a "-b hybrid mcuUdid"获取设备的UDID。
