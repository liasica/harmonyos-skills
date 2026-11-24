---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-screen-mirroring
title: 设备投屏
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 设备投屏
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:30+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:924747c274bf66ce7408e0506074f299808e47105451d84f95f4dd23301f0e7d
---

从26.0.0版本开始，新增设备投屏功能，支持对已连接的设备进行投屏操作，方便查看设备屏幕内容并进行设备操控，提升开发调试效率。

## 使用约束

* 仅支持HarmonyOS设备（穿戴设备除外），并且已通过USB或Wi-Fi连接设备。
* 该功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

## 操作步骤

1. 在DevEco Studio下方点击**Screen Mirroring，**或点击菜单栏**View > Tool Windows >** **Screen Mirroring**，打开设备投屏窗口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/2YTEg6sCRPilBZhqT-5Mwg/zh-cn_image_0000002779566970.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=3683A0AE3DBB3BBD872A214AB27AB74B7B320C8B5046EB20B9F6FFA98BB9428C)
2. 从设备下拉列表中选择设备（设备需已连接），点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/bSwvtsKDQ8Cgz-FsN02fdQ/zh-cn_image_0000002779406994.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=57D0F3AF25159D238902A8324DEA8F9EBB5C16A4E5C7020E0EED9D4DD0A743D6)按钮开始投屏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/62sjCl3oTAKxPBh9Q-Wa9w/zh-cn_image_0000002779406992.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=4C7F845D148B0972906D80486447AF84A34F8105ADFC0765A20DFAF9DBA27939)
3. 设备投屏后，支持对设备进行如下操作：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/4thRxhvkRFe7Z_qA9nR0XA/zh-cn_image_0000002779566972.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=3C71EE128FB322B394464728D3DB5DE3B270C5C7AE3A7111F4B9091A80BC5053)：停止投屏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/Fn_fiaZ3RM6yFAPR2VrzIg/zh-cn_image_0000002808886623.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=9EEE0DB36765D0E4D36CF10A8E908E3521BF3ED97FBBE3B212A423A515C7AB3F)：刷新重连设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/hW9r9aaKRVORUs4OxkwOGA/zh-cn_image_0000002808886625.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=94C6F531FD72DA405FC35257AF25B0F35B426F3315550519FD0475EE86BFC426)：对应设备返回键，返回上一屏幕或退出应用等。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/h86p9yUAR1iQ8KHDJ8xTDg/zh-cn_image_0000002808766549.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=F4A59E61916D307B41D0BE081BCD5E01F3A23B9A30711604D1257BED5209929C)：查看最近使用的应用列表。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/SATbovOPQQSYifCyGk2qOw/zh-cn_image_0000002808886627.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=7EB5EACBF2ADD85909CB8548F744DC19D61B28E7D068B6F40C1D5F04CFDD7BB7)：对应Home键，返回主屏幕。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/6lv9M-d6RQKGkdmX3F1ytQ/zh-cn_image_0000002808766543.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=508A8B780248F9FD7F5D81FA3E1D29DD88E128D51A68FC8B733F8548A02EF80F)：对应电源键，可以锁屏和亮屏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/JYO9rqSXQvCfT3FNu_ENXw/zh-cn_image_0000002779406988.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=0C606D307418F9E9DC2F8F68907EC4C1DBE380EFCBA7990778D9399BE7C64E49)：屏幕点击模式，默认为鼠标模式，点击按钮后切换为触摸屏模式，同时图标切换为![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/yTymdYn4TRWOzqDn0SpU_A/zh-cn_image_0000002808766545.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=0AEDCF5176B32E8A87186D58B07E9D3EC857EB7DA84C5B7A1CAB40BC468EC138)。
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
