---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-start-and-close
title: 启动和关闭模拟器
breadcrumb: 指南 > 编写与调试应用 > 使用模拟器运行应用 > 管理模拟器 > 启动和关闭模拟器
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:16+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3a065dbf4f7d181d881e2c2f42b7fb79300336e1d13a0d139906ba30f758810d
---

在设备管理器页面，单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/3Xmf2z-XTZux0LOgTLMxkQ/zh-cn_image_0000002701661932.png)即可启动模拟器。模拟器启动时会默认携带之前运行时的用户数据，包括用户上传的文件，安装的应用等。如果是新创建的模拟器，则不会携带用户数据。如果想清除之前运行时的用户数据，点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/RLe_xQAZTKaAI7fA8CS8Pw/zh-cn_image_0000002731541117.png) **> Wipe User Data**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/yCjEE0hSTg2EuMR_DVS8TQ/zh-cn_image_0000002701821860.png "点击放大")

从DevEco Studio 6.1.0 Beta1版本开始，如果创建模拟器时选择热启动，则启动模拟器时会加载上次关闭时保存的快照，启动后会恢复至上次关闭时的状态。热启动后，多屏状态会恢复为单屏状态。

从26.0.0版本开始，如果热启动后出现异常，可点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/g3pT-5VLQbW3CytnsqM-tg/zh-cn_image_0000002731541139.png) **> Cold Boot**，本次将以冷启动方式启动模拟器，并且会保留之前的用户数据，关闭模拟器时仍会保存快照。

例如推包运行后关闭模拟器，再次启动时会显示在上次运行的界面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/Vis_E7NQSTaK894zThJKpg/zh-cn_image_0000002731381189.png "点击放大")

在模拟器运行期间，可以点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/9Z-JUEODRPi-uWSRGVZueg/zh-cn_image_0000002701821874.png) **> Show on Disk**显示模拟器在本地生成的用户数据。点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/Z8W0-2oBQg6b8J9xVb2mtw/zh-cn_image_0000002701821854.png) **> Generate logs**可以生成模拟器自启动到此刻的所有日志信息。想要关闭运行中的模拟器，可以在设备管理器页面点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/ZMRHS-G9SAetSoroFlSRfQ/zh-cn_image_0000002731541111.png)，或者点击模拟器工具栏上的关闭按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/EwKQakTPRzieYksyKxBjvQ/zh-cn_image_0000002731541163.png)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/PEZGrOM0QPqH4gzFXkdhow/zh-cn_image_0000002731381151.png "点击放大")

模拟器关闭后，点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/HnCGnvNjS_-g-SDADlwpbg/zh-cn_image_0000002731541153.png) **> Delete**可以删除模拟器，并清除模拟器的用户数据和配置信息。
