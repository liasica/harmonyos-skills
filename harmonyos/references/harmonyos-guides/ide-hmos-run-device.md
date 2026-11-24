---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-run-device
title: 使用本地真机运行应用
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 使用本地真机运行应用
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:45+08:00
doc_updated_at: 2026-11-06
content_hash: sha256:5c3453143ec42a7612f7ba43fbd5821ade89a192d35804fe8b8ded07f1b10c74
---

鸿蒙电脑DevEco Studio允许开发者连接本地真机运行HarmonyOS应用/元服务，可以采用USB连接方式或者无线连接方式。

**说明** 

Wearable设备仅支持无线连接方式（Lite Wearable设备不支持）。

## 前提条件

* 在真机设备上查看**设置** **> 系统**中**开发者选项**是否存在，如果不存在，可在**设置 > *具体的设备名称***中，连续七次单击**软件****版本**，直到提示“开启开发者选项”，点击**确认开启**后输入PIN码（如果已设置），设备将自动重启，请等待设备完成重启。
* 2in1设备需要确保关闭反向超级快充模式，在该模式下不支持通过USB调试设备。在2in1设备的通知中心查看提示并关闭。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/_RhM3HqoRViunO8sKULbtg/zh-cn_image_0000002820681163.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=AB8EB6BD8670B5551CF89E9BD0AF068B8C432D9B89478ED11692865E087B67D8)
* 在设备运行应用/元服务需要根据[配置调试签名](ide-hmos-signing.md)章节，提前对应用/元服务进行签名。

## 使用USB连接方式

1. 使用USB方式，将真机设备与2in1设备进行连接。
2. 在**设置 > 系统 > 开发者选项**中，打开**USB调试**开关（确保设备已连接USB）。
3. 在真机设备中会弹出“允许USB调试”的弹框，单击**允许**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/SA8gQxxpR2OPNOohavk9hQ/zh-cn_image_0000002820681161.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=C78983811E62A38563F24C2B1C591EEC5C92B5EB0BE5CD1135A33D4EEA065BAD)
4. 在界面上方选择模块后，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/y87DjjiIRke6ePLfUUr1gw/zh-cn_image_0000002791841226.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=93F10CA7DDA4A88AB3E9802D1D69060E06D910E7594296715A24B0F725434446)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/0XVigQ9zSL2HRAVyHNLkoA/zh-cn_image_0000002820721161.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=216BFC711F8FA9B0E0115D9C35301A2CCAE14A20846011BC05CD64D294032113)
5. DevEco Studio启动HAP的编译构建和安装。安装成功后，设备会自动运行安装的HarmonyOS应用/元服务。

**说明** 

如果DevEco Studio无法识别到已连接的设备，可参考[真机设备识别常见问题](../harmonyos-faqs/app-debugging-faq-0012.md)。

## 使用无线连接方式

1. 将真机设备和PC连接到同一WLAN网络。
2. 在**设置 > 系统 >** **开发者选项**中，打开**无线调试**或**通过WLAN调试**（Wearable设备）开关，并获取设备端的IP地址和端口号。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/dGDmwq9vQCeKNB1aR9b46Q/zh-cn_image_0000002791841228.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=3C706FC68641D7A7F55056C0FF22A9DA2120175092090B600EBC6E3917C48BE7 "点击放大")
3. 连接设备，有两种方式。
   * 通过DevEco Studio连接。

     在设备下拉列表单击**无线连接**，按照IP:port格式输入设备的IP地址和端口号，单击**连接**按钮连接设备，连接成功后会显示在列表中，默认开启屏幕常亮。

     开启屏幕常亮后，DevEco Studio会持续向设备发送亮屏指令，使设备屏幕常亮。即使手动将设备锁屏，屏幕也会自动亮起，这是DevEco Studio为保持屏幕常亮而发送亮屏指令的正常行为。

     如需退出屏幕常亮，有以下方式：

     + 方式一：在无线连接面板中单击**停止屏幕常亮**。
     + 方式二：断开设备连接。

     退出后，DevEco Studio将停止发送亮屏指令，设备可正常进入休眠。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/B9eTboSqTB6BcvhY1nDeUA/zh-cn_image_0000002792001202.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=6A342AB152A235145D2A94B84CF896C678C99FA2C90F20DB20B65D38ACB13A4B)
   * 通过hdc连接，关于hdc工具的使用指导请参考[hdc](hdc.md)。

     ```bash
     hdc tconn 设备IP地址:端口号
     ```
4. 在界面上方选择模块后，单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/QUITBuKMShKTleEx7MWASQ/zh-cn_image_0000002791841224.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=AB20AEA32C6F8EED006C3BDB53F405D141621690BD6452D733D8BEEE377E74FE)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/NufbA0HbSp-wiaOXcfUVTA/zh-cn_image_0000002820681159.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=36ED0556D8C41180BACD8ED5C6C14D30E4303C2A9908127CBEC90A9B0F82BBB5)
5. DevEco Studio启动HAP的编译构建和安装。安装成功后，设备会自动运行安装的HarmonyOS应用/元服务。
