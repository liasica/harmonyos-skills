---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-run-device
title: 使用本地真机运行应用
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 使用本地真机运行应用
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:55+08:00
doc_updated_at: 2026-11-06
content_hash: sha256:93d8bbde0168b10108a9ccf3f3585d6df64240eeb1461033d9568b1bbdf5ba42
---

鸿蒙电脑DevEco Studio允许开发者连接本地真机运行HarmonyOS应用/元服务，可以采用USB连接方式或者无线连接方式。

**说明** 

Wearable设备仅支持无线连接方式（Lite Wearable设备不支持）。

## 前提条件

* 在真机设备上查看**设置** **> 系统**中**开发者选项**是否存在，如果不存在，可在**设置 > *具体的设备名称***中，连续七次单击**软件****版本**，直到提示“开启开发者选项”，点击**确认开启**后输入PIN码（如果已设置），设备将自动重启，请等待设备完成重启。
* 2in1设备需要确保关闭反向超级快充模式，在该模式下不支持通过USB调试设备。在2in1设备的通知中心查看提示并关闭。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/hLpjCTPhQByXgr85w7V3PA/zh-cn_image_0000002820681163.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=EC1289D915234DE9A7F0D106F69EBA44BE88A1D68BE53DFD79E4766252205465)
* 在设备运行应用/元服务需要根据[配置调试签名](ide-hmos-signing.md)章节，提前对应用/元服务进行签名。

## 使用USB连接方式

1. 使用USB方式，将真机设备与2in1设备进行连接。
2. 在**设置 > 系统 > 开发者选项**中，打开**USB调试**开关（确保设备已连接USB）。
3. 在真机设备中会弹出“允许USB调试”的弹框，单击**允许**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/TaKw5diyTwKEXbr4uLCb5Q/zh-cn_image_0000002820681161.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=3EBE37D39EC78985C3DCDD48E5A2E655ACE6A70A9EC88F84851919437189E966)
4. 在界面上方选择模块后，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/tDUzjKYhTyGoUsH0vE7r3g/zh-cn_image_0000002791841226.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=48EBBF4E967B05E4B6D9A271FDCA13C5088CFACA532A23F453B122BCA33871B2)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/51wPh-PrRIG2TrPy4Mmu1g/zh-cn_image_0000002820721161.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=4BDEC3EBE0D15E95F8DD5E685B6024C8E7B712F506735099D81678A6DDBC512A)
5. DevEco Studio启动HAP的编译构建和安装。安装成功后，设备会自动运行安装的HarmonyOS应用/元服务。

**说明** 

如果DevEco Studio无法识别到已连接的设备，可参考[真机设备识别常见问题](../harmonyos-faqs/app-debugging-faq-0012.md)。

## 使用无线连接方式

1. 将真机设备和PC连接到同一WLAN网络。
2. 在**设置 > 系统 >** **开发者选项**中，打开**无线调试**或**通过WLAN调试**（Wearable设备）开关，并获取设备端的IP地址和端口号。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/Ymk2DdDeR8mUJRuzzcNGYA/zh-cn_image_0000002791841228.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=E6C6E5855CB6C4B849E615ACEE21CE34B1C559A478572ED724D2800A00DFD57B "点击放大")
3. 连接设备，有两种方式。
   * 通过DevEco Studio连接。

     在设备下拉列表单击**无线连接**，按照IP:port格式输入设备的IP地址和端口号，单击**连接**按钮连接设备，连接成功后会显示在列表中，默认开启屏幕常亮。

     开启屏幕常亮后，DevEco Studio会持续向设备发送亮屏指令，使设备屏幕常亮。即使手动将设备锁屏，屏幕也会自动亮起，这是DevEco Studio为保持屏幕常亮而发送亮屏指令的正常行为。

     如需退出屏幕常亮，有以下方式：

     + 方式一：在无线连接面板中单击**停止屏幕常亮**。
     + 方式二：断开设备连接。

     退出后，DevEco Studio将停止发送亮屏指令，设备可正常进入休眠。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/Ek2M6746QIOCN26Hsrx1dA/zh-cn_image_0000002792001202.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=A2C8E3358F3AC724ACA4985F0FA325A3D9A9A818A6E7CE64FE14A01D5D0B2258)
   * 通过hdc连接，关于hdc工具的使用指导请参考[hdc](hdc.md)。

     ```bash
     hdc tconn 设备IP地址:端口号
     ```
4. 在界面上方选择模块后，单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/sNR9vnbORMmMlECWxIPbQQ/zh-cn_image_0000002791841224.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=0E1B63F12B988D964981BE6E87C238AF29E18A1DD53AF9C5558846C21D2E59FA)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/3qemcXx1R0aKeHndIir8Vw/zh-cn_image_0000002820681159.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=20D74DB8FB5596F4BDF554418C707D4F29A142C8172FCDFAE971DCF0FCBED212)
5. DevEco Studio启动HAP的编译构建和安装。安装成功后，设备会自动运行安装的HarmonyOS应用/元服务。
