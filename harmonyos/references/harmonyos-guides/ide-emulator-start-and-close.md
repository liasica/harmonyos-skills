---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-start-and-close
title: 启动和关闭模拟器
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 使用模拟器运行应用 > 管理模拟器 > 启动和关闭模拟器
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:34974428617ca52d4f7d1d8cfdea2b199b8ebd31f9eada56bee33e8efe35865f
---

在设备管理器页面，单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/dhhuuBvxTBCLjUPirEqVug/zh-cn_image_0000002779405122.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=46B9383E4773E7E090F106061F23F3F4D442C3A66F66752DE315B8C7ECB73D8E)即可启动模拟器。模拟器启动时会默认携带之前运行时的用户数据，包括用户上传的文件，安装的应用等。如果是新创建的模拟器，则不会携带用户数据。如果想清除之前运行时的用户数据，点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/MdB2kLG-Qiq7P449LVoMyA/zh-cn_image_0000002808764673.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=D16785C6F102509ABA51EFB3A8D474889916FE648BDC7B46473DC871361BB575) **> Wipe User Data**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/vn4OpCZaQmKATOS6MdRZbA/zh-cn_image_0000002779565078.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=9C49A8B6E5E9AA46B4F1B71B929000A3AC5C4B66EAE96D7A9DA86445BE68B0BF "点击放大")

从DevEco Studio 6.1.0 Beta1版本开始，如果创建模拟器时选择热启动，则启动模拟器时会加载上次关闭时保存的快照，启动后会恢复至上次关闭时的状态。热启动后，多屏状态会恢复为单屏状态。

从26.0.0版本开始，如果热启动后出现异常，可点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/3ZrGGCG5SO6y9YX-uZaVVg/zh-cn_image_0000002779405132.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=39919B19A582962EBD4781B1DA02DCC1CBF69060758C17011840E8910D9B5E1A) **> Cold Boot**，本次将以冷启动方式启动模拟器，并且会保留之前的用户数据，关闭模拟器时仍会保存快照。

例如推包运行后关闭模拟器，再次启动时会显示在上次运行的界面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/vAifTplMSRWhMUyx9WRkcA/zh-cn_image_0000002808884783.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=9298319638322AE36D113AE9B43CEA679161506EA1E7DE859CF7D778E43AB9E7 "点击放大")

在模拟器运行期间，可以点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/m-qNiSrQQQe77UnJOqyy2w/zh-cn_image_0000002779565086.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=FAE1B7468F851B1CDDD9B5B092D32038AF734162F090EC13D77DE030E55A7C62) **> Show on Disk**显示模拟器在本地生成的用户数据。点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/yVio7cpWSzC6WZ_8yMViAA/zh-cn_image_0000002808764655.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=F755FD551E9A70B60BE111C969D58895EC4A6C7529479F6985D1E2E179B27E85) **> Generate logs**可以生成模拟器自启动到此刻的所有日志信息。想要关闭运行中的模拟器，可以在设备管理器页面点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/-EFU9T0zT_SHnSsyPkwssQ/zh-cn_image_0000002779405144.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=3CDD84645536A20BF8DFFE1E5F6B5CC3E43AFEA50378DA842D6BEEBE0652252C)，或者点击模拟器工具栏上的关闭按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/BSCEekxFQc-wW7liZ4Uh3A/zh-cn_image_0000002779405130.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=C9F17599245BC6F02B18262BF2F10E53B40242E858F08B2EDE4DCBF93FC59F82)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/uY1BaqCNTGS6LUdrzfdkfA/zh-cn_image_0000002808884733.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=AA91D86482C0557DB5E89244F7F1717BA52EB3204FF044A0E00B2B9E3546F6DA "点击放大")

模拟器关闭后，点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/z3n9OlrfQoWANsmtvhBHUA/zh-cn_image_0000002779405126.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=8A39D55C9BDBFC118759DC370C5758E5D3D263BA9ACD767FF8C3C5D5D955E291) **> Delete**可以删除模拟器，并清除模拟器的用户数据和配置信息。
