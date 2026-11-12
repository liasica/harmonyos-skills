---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-run-device
title: 使用本地真机运行应用
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 使用本地真机运行应用
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-06
content_hash: sha256:5c821785dde0821328855eccde1403531bae8d5f4c8c2c2c6a73ec8000745261
---

鸿蒙电脑DevEco Studio允许开发者连接本地真机运行HarmonyOS应用/元服务，可以采用USB连接方式或者无线连接方式。

**说明** 

Wearable设备仅支持无线连接方式（Lite Wearable设备不支持）。

## 前提条件

* 在真机设备上查看**设置** **> 系统**中**开发者选项**是否存在，如果不存在，可在**设置 > *具体的设备名称***中，连续七次单击**软件****版本**，直到提示“开启开发者选项”，点击**确认开启**后输入PIN码（如果已设置），设备将自动重启，请等待设备完成重启。
* 2in1设备需要确保关闭反向超级快充模式，在该模式下不支持通过USB调试设备。在2in1设备的通知中心查看提示并关闭。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/fjyV8g2eTeCBDpZI2-pJ5Q/zh-cn_image_0000002781311188.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=E7591C57354967DD312C87288DC9B8D8BDF4568664173338B0C501B0580C8BD6)
* 在设备运行应用/元服务需要根据[配置调试签名](ide-hmos-signing.md)章节，提前对应用/元服务进行签名。

## 使用USB连接方式

1. 使用USB方式，将真机设备与2in1设备进行连接。
2. 在**设置 > 系统 > 开发者选项**中，打开**USB调试**开关（确保设备已连接USB）。
3. 在真机设备中会弹出“允许USB调试”的弹框，单击**允许**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/MozcSaMtQFGMy1gsod17Vg/zh-cn_image_0000002781471124.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=C3908F8F7C7B0E368BA377E88B9B95F2ED229A5522DED3419A0BBC1A0CB71071)
4. 在界面上方选择模块后，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/grHdgN9cQAuaPcFyhQp6ng/zh-cn_image_0000002781471128.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=89F6905E3E148D941A833279F9889AFC82496BB6EAB57F13466206007C8594C5)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/7CK_i2W2TymqjGwvM4FuhA/zh-cn_image_0000002810750787.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=434F5EE4028C52B33EBB37DDE6D4390D8777144F69CDCF8B90CBA295EDD3D1FA)
5. DevEco Studio启动HAP的编译构建和安装。安装成功后，设备会自动运行安装的HarmonyOS应用/元服务。

**说明** 

如果DevEco Studio无法识别到已连接的设备，可参考[真机设备识别常见问题](../harmonyos-faqs/app-debugging-faq-0012.md)。

## 使用无线连接方式

1. 将真机设备和PC连接到同一WLAN网络。
2. 在**设置 > 系统 >** **开发者选项**中，打开**无线调试**或**通过WLAN调试**（Wearable设备）开关，并获取设备端的IP地址和端口号。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/BG6TDZ5ySpSn_Ccys61ptQ/zh-cn_image_0000002781311186.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=AB2536375D08FF402CC17DE6EE868DB8FCB09F3272A7D0BB0EC7A2703E79908A "点击放大")
3. 连接设备，有两种方式。
   * 通过DevEco Studio连接。

     在设备下拉列表单击**无线连接**，按照IP:port格式输入设备的IP地址和端口号，单击**连接**按钮连接设备，连接成功后会显示在列表中，默认开启屏幕常亮。

     开启屏幕常亮后，DevEco Studio会持续向设备发送亮屏指令，使设备屏幕常亮。即使手动将设备锁屏，屏幕也会自动亮起，这是DevEco Studio为保持屏幕常亮而发送亮屏指令的正常行为。

     如需退出屏幕常亮，有以下方式：

     + 方式一：在无线连接面板中单击**停止屏幕常亮**。
     + 方式二：断开设备连接。

     退出后，DevEco Studio将停止发送亮屏指令，设备可正常进入休眠。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/lEbCEWL3Q3uhkY6exfPvSg/zh-cn_image_0000002810630679.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=D9EA309709250ACDEC5B24B8AEDC3DD432B11EF9CDFC4FEA23B32FD2753B9AF1)
   * 通过hdc连接，关于hdc工具的使用指导请参考[hdc](hdc.md)。

     ```bash
     hdc tconn 设备IP地址:端口号
     ```
4. 在界面上方选择模块后，单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/PtiIZGGYRRijSGaDHDaT_g/zh-cn_image_0000002781311190.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=D2110FBAAF1B9441FDEB87658F6BAC83E3A0628344489D297908ED422037AD1A)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/XgE9cfDkTFeg-Nj9i2G_TQ/zh-cn_image_0000002781471122.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=16E7EF56A48245D0FCB6B728B945F80F94CD7EF915E819E47D7FB1D51C09FD39)
5. DevEco Studio启动HAP的编译构建和安装。安装成功后，设备会自动运行安装的HarmonyOS应用/元服务。
