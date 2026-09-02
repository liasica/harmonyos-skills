---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-start-and-close
title: 启动和关闭模拟器
breadcrumb: 指南 > 编写与调试应用 > 使用模拟器运行应用 > 管理模拟器 > 启动和关闭模拟器
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fb0202f3b36cb9b57e705996c8386e1eba133cc067dbc028b22d55ab926e4d60
---

在设备管理器页面，单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/AnV_WH7DSMmamHjocEU4EA/zh-cn_image_0000002530911082.png)即可启动模拟器。模拟器启动时会默认携带之前运行时的用户数据，包括用户上传的文件，安装的应用等。如果是新创建的模拟器，则不会携带用户数据。如果想清除之前运行时的用户数据，点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/26Y9zmDJRUaGtdutwiXBig/zh-cn_image_0000002561831005.png) **> Wipe User Data**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/MvoeCqV5S-qV25gvt5t0Zg/zh-cn_image_0000002530751076.png "点击放大")

从DevEco Studio 6.1.0 Beta1版本开始，如果创建模拟器时选择热启动，则启动模拟器时会加载上次关闭时保存的快照，启动后会恢复至上次关闭时的状态。热启动后，多屏状态会恢复为单屏状态，折叠屏模拟器会恢复成默认展开状态。

如果热启动后出现异常，可点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/DqiS3wctRtey2FjUsOTWOw/zh-cn_image_0000002561751033.png) **> Wipe User Data**清除用户数据后重新启动。

例如推包运行后关闭模拟器，再次启动时会显示在上次运行的界面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/_APTZilzS5iM7uoznzcnsQ/zh-cn_image_0000002530911092.png "点击放大")

在模拟器运行期间，可以点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/zatSxaCBQt2UsQ3id72cbw/zh-cn_image_0000002561751025.png) **> Show on Disk**显示模拟器在本地生成的用户数据。点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/u7mppL6qTcauxfiH2kH8Nw/zh-cn_image_0000002561751021.png) **> Generate logs**可以生成模拟器自启动到此刻的所有日志信息。想要关闭运行中的模拟器，可以在设备管理器页面点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/nv1-t1RVS1OG8_CVSxPcxw/zh-cn_image_0000002530751080.png)，或者点击模拟器工具栏上的关闭按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/ITvbPefPT4W_BJZGiINKew/zh-cn_image_0000002530751090.png)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/kz6jd6uKR3KOPm97eL4aIQ/zh-cn_image_0000002561751013.png "点击放大")

模拟器关闭后，点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/JHCHZwVjS9OFdRsknp7c5w/zh-cn_image_0000002530911084.png) **> Delete**可以删除模拟器，并清除模拟器的用户数据和配置信息。
