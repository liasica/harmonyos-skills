---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-screen-mirroring
title: 设备投屏
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 设备投屏
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:00+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:7f0ebc500ee5562e3b8b2211958dd9bc0428a00ada7f5f819cae80ff1afa57fe
---

从26.0.0版本开始，新增设备投屏功能，支持对已连接的设备进行投屏操作，方便查看设备屏幕内容并进行设备操控，提升开发调试效率。

## 使用约束

* 仅支持HarmonyOS设备（穿戴设备除外），并且已通过USB或Wi-Fi连接设备。
* 该功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

## 操作步骤

1. 在DevEco Studio下方点击**Screen Mirroring，**或点击菜单栏**View > Tool Windows >** **Screen Mirroring**，打开设备投屏窗口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/UiBpF30vTpKqieq7n8u8zA/zh-cn_image_0000002779566970.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=1E204A0E5E4E5ECEC7F6317371CD96AFBAC2A9537383716DBB808C9C317F9B7C)
2. 从设备下拉列表中选择设备（设备需已连接），点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/pJ1ZWJUXR46Cxq6oQ9mvjg/zh-cn_image_0000002779406994.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=00806C7378C64861346511133C2F8D4549F832562B7735BAE47387422D6CEFAE)按钮开始投屏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/YhOTWWhvSNWm2YmwzIdwgQ/zh-cn_image_0000002779406992.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=43B54C4A3DB150B16450D77DEF92F290B49308E0FFC45DFF41D71B898D29E56E)
3. 设备投屏后，支持对设备进行如下操作：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/TlTaPSWAQWGM9C79xaWBjQ/zh-cn_image_0000002779566972.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=6541E30A0CA6923ABACBCDDECF832013256A78B9E9C189500A867822A969BF8A)：停止投屏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/GeBGwrGpTcSNR9NMDUDx_A/zh-cn_image_0000002808886623.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=1B9427C41FA351ADEEC66FBFC322E2710B62651888B4532713F2146D2994A231)：刷新重连设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/Ho2ikGOXQtmeAvMVimo7RA/zh-cn_image_0000002808886625.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=AC2BF7A3A37D3FDEDEA5F3DF8B31F62ED2FA44FAA7926F3B6BC82B825670B176)：对应设备返回键，返回上一屏幕或退出应用等。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/vJ4yjT_sTtezMcNs6Fy3bQ/zh-cn_image_0000002808766549.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=375CA79F45CEBF2F48C9CD3510F1353B932632ABFEE56E08B5F9C21CBE1CDA8B)：查看最近使用的应用列表。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/OBkGFjO1Q7m-ia4WpuBOWA/zh-cn_image_0000002808886627.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=7C06C4DF0EFB6FA9904D5F3B6084B46A2F7B1FFD237A4BCE7EF424C3D2D6CC04)：对应Home键，返回主屏幕。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/GAo2Qn8YR8K3JnCKcy6cNg/zh-cn_image_0000002808766543.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=F36AAD462D1FB44F5DFDE1ECBE8706D5E81BC6F24C09273D683CEC60EC11C4B3)：对应电源键，可以锁屏和亮屏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/JHvGWCVATJygqhP6SmY0dg/zh-cn_image_0000002779406988.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=A4FA2BA5526B6BCC85E8CA85712170556B46A0DAA9C0917A50FC0A65676AD995)：屏幕点击模式，默认为鼠标模式，点击按钮后切换为触摸屏模式，同时图标切换为![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/4c1JidJQS_yPeL3a3Uk--w/zh-cn_image_0000002808766545.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=D24B3DFF72FD82B0AF6B27258ACBAA6015DC5F2A00C1B0BED7011A4F636B4AB6)。
4. 支持使用鼠标操控屏幕、使用键盘输入等，具体参考下文介绍。

## 操控屏幕

支持使用鼠标来模拟手指/鼠标与设备屏幕界面进行交互的场景。

| 常用操作 | 描述 |
| --- | --- |
| 单击屏幕 | 单击鼠标左键可以模拟点击操作，如点击应用图标等。 |
| 双击屏幕 | 双击鼠标左键可以模拟在2in1设备上的双击操作，如双击应用图标等。 |
| 单击/长按右键 | 单击/长按鼠标右键可以弹出菜单，操作方式和设备上弹出菜单的方式一致，例如设备上是通过长按弹出菜单的，在投屏中也通过长按鼠标右键弹出菜单。 |
| 拖动项目 | 长按鼠标左键可以模拟长按操作，例如长按图标进行拖动。 |
| 滑动屏幕 | 按下鼠标左键并滑动可以模拟滑动操作，鼠标模式下可用于选择文本等，触摸屏模式下可用于滚动列表、翻页等。 |

## 使用键盘输入

鼠标点击输入框，可以使用计算机键盘输入字符到设备上。

## 安装应用和上传文件

通过拖拽文件可以安装应用和上传文件到设备上。

* **安装应用：**拖拽HAP/HSP包会自动安装到设备上，支持一次性拖拽安装多个HAP/HSP包。
* **上传文件：**支持将本地文件上传到设备中，只需将文件拖拽到屏幕即可。支持批量上传，上传的文件存放在设备的/storage/media/100/local/files/Docs/Download/目录下，同名文件会覆盖，如果文件总大小过大（10G以上）可能会上传失败。上传文件后，可以在设备的**文件管理 > 我的手机 > 下载**中查看。
