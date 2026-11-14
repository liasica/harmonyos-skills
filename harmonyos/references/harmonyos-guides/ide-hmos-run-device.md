---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-run-device
title: 使用本地真机运行应用
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 使用本地真机运行应用
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:16+08:00
doc_updated_at: 2026-11-06
content_hash: sha256:919c0567ad0c0101565a92665fc8e98253d0d2c254bad6481d5785b6e94a167c
---

鸿蒙电脑DevEco Studio允许开发者连接本地真机运行HarmonyOS应用/元服务，可以采用USB连接方式或者无线连接方式。

**说明** 

Wearable设备仅支持无线连接方式（Lite Wearable设备不支持）。

## 前提条件

* 在真机设备上查看**设置** **> 系统**中**开发者选项**是否存在，如果不存在，可在**设置 > *具体的设备名称***中，连续七次单击**软件****版本**，直到提示“开启开发者选项”，点击**确认开启**后输入PIN码（如果已设置），设备将自动重启，请等待设备完成重启。
* 2in1设备需要确保关闭反向超级快充模式，在该模式下不支持通过USB调试设备。在2in1设备的通知中心查看提示并关闭。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/Da1MSJs1RCiSpnmjE-Zoxg/zh-cn_image_0000002781311188.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=B11C12197FC4AB1CAFCA0FAF223215F5161D86680A3B08E9A3F816A5ABCE9F0D)
* 在设备运行应用/元服务需要根据[配置调试签名](ide-hmos-signing.md)章节，提前对应用/元服务进行签名。

## 使用USB连接方式

1. 使用USB方式，将真机设备与2in1设备进行连接。
2. 在**设置 > 系统 > 开发者选项**中，打开**USB调试**开关（确保设备已连接USB）。
3. 在真机设备中会弹出“允许USB调试”的弹框，单击**允许**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/pzur7b1ORbSE7Bn_16MYvw/zh-cn_image_0000002781471124.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=7DDB2F2996D36B56BBE2C54FF94526BE6730534C524DEFEF8431AF3FFB82D4FE)
4. 在界面上方选择模块后，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/ks7nujEJQAW0QL1qii1xkA/zh-cn_image_0000002781471128.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=8176B56E0E7846F84E4C8E6B629CFB2C839C502CDB4E3B7A00E9BF61822FD15A)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/wd2DPaSeQpSQkUEuuY9xcw/zh-cn_image_0000002810750787.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=FF7B29199A4138040D2E3C923081F3CC1846A1042A6F0394EE332F6862A72B10)
5. DevEco Studio启动HAP的编译构建和安装。安装成功后，设备会自动运行安装的HarmonyOS应用/元服务。

**说明** 

如果DevEco Studio无法识别到已连接的设备，可参考[真机设备识别常见问题](../harmonyos-faqs/app-debugging-faq-0012.md)。

## 使用无线连接方式

1. 将真机设备和PC连接到同一WLAN网络。
2. 在**设置 > 系统 >** **开发者选项**中，打开**无线调试**或**通过WLAN调试**（Wearable设备）开关，并获取设备端的IP地址和端口号。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/3YZmmFZSQRyYegyJymd6Bg/zh-cn_image_0000002781311186.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=A34AF566C334489809F3A9845128EE9A468B43F0CDA6EA8250C2060966D97671 "点击放大")
3. 连接设备，有两种方式。
   * 通过DevEco Studio连接。

     在设备下拉列表单击**无线连接**，按照IP:port格式输入设备的IP地址和端口号，单击**连接**按钮连接设备，连接成功后会显示在列表中，默认开启屏幕常亮。

     开启屏幕常亮后，DevEco Studio会持续向设备发送亮屏指令，使设备屏幕常亮。即使手动将设备锁屏，屏幕也会自动亮起，这是DevEco Studio为保持屏幕常亮而发送亮屏指令的正常行为。

     如需退出屏幕常亮，有以下方式：

     + 方式一：在无线连接面板中单击**停止屏幕常亮**。
     + 方式二：断开设备连接。

     退出后，DevEco Studio将停止发送亮屏指令，设备可正常进入休眠。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/XXjBoGK-SbStYPxjY5Y93A/zh-cn_image_0000002810630679.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=A461D2D19C5B00CDF0084A86BA6DBF9D85CEA2E56F18EB3DB91CD77BF93EF14C)
   * 通过hdc连接，关于hdc工具的使用指导请参考[hdc](hdc.md)。

     ```bash
     hdc tconn 设备IP地址:端口号
     ```
4. 在界面上方选择模块后，单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/Xc5slAbZQkyxSi_llEql7A/zh-cn_image_0000002781311190.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=2FA74CEB69C5F0ECC2131E91D5091F590A376177D276A1D770311FBC3E6FFB3A)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/3XW5PcLnT6O50FPH0QpUwQ/zh-cn_image_0000002781471122.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=CDE67924619DD435D2E4DBBCC6288CD6FD7309E9B0B82A8B07FDC012CB621EDE)
5. DevEco Studio启动HAP的编译构建和安装。安装成功后，设备会自动运行安装的HarmonyOS应用/元服务。
