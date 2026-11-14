---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-start-and-close
title: 启动和关闭模拟器
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 使用模拟器运行应用 > 管理模拟器 > 启动和关闭模拟器
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:58+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:264402df8b4f6924db0613a01a10afef8c2e5f365cd06dffa919768912c18d3b
---

在设备管理器页面，单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/OPdP-ruHQt6crvXTKkaPmA/zh-cn_image_0000002779405122.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=23C89063DA3A78B665763E63E4E4BDEFDE8FDB0BAAD51B5E4C6412D7C13217A7)即可启动模拟器。模拟器启动时会默认携带之前运行时的用户数据，包括用户上传的文件，安装的应用等。如果是新创建的模拟器，则不会携带用户数据。如果想清除之前运行时的用户数据，点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/FAirsTvUSoeOtfcPFddVOw/zh-cn_image_0000002808764673.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=9FAFD768DD4D50E7560D1E9C7C33DBCB977D7EDFE21A9F0C7B64D405A6F473AC) **> Wipe User Data**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/dlvAIf7TRZKyPWTqXuJPdQ/zh-cn_image_0000002779565078.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=6683676B005D7655505F82154BB2FB8EB30531FE8E9EB42D037606E9269741AB "点击放大")

从DevEco Studio 6.1.0 Beta1版本开始，如果创建模拟器时选择热启动，则启动模拟器时会加载上次关闭时保存的快照，启动后会恢复至上次关闭时的状态。热启动后，多屏状态会恢复为单屏状态。

从26.0.0版本开始，如果热启动后出现异常，可点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/8QPq9YL7Sf2Z9_QsiWjn8g/zh-cn_image_0000002779405132.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=3DD702BA27EF12E842A24F57B1B5162055AD64C44A5D894EBEC1D9AB42B39D15) **> Cold Boot**，本次将以冷启动方式启动模拟器，并且会保留之前的用户数据，关闭模拟器时仍会保存快照。

例如推包运行后关闭模拟器，再次启动时会显示在上次运行的界面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/VcZtVmJsTMGXuMLB6Z4RpQ/zh-cn_image_0000002808884783.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=27FB2824E00AFB74B5A739B2B5013B606106611A53A69E7B02D6F7C295DC6F3C "点击放大")

在模拟器运行期间，可以点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/eFo4EX08Rk-TSnjiEfz0CA/zh-cn_image_0000002779565086.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=EB290A30BA2894BC2649634351317928F7E2336355E8B0ADF2BBB56365383D6B) **> Show on Disk**显示模拟器在本地生成的用户数据。点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/Ykuv8bZLT1uE34nwsKIfEQ/zh-cn_image_0000002808764655.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=E314B9484156B19B839DB452FF328BC01BAF55ECAF1F8F70193903B52E4AF5E4) **> Generate logs**可以生成模拟器自启动到此刻的所有日志信息。想要关闭运行中的模拟器，可以在设备管理器页面点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/Yphju3rSSi6NfSlYAfDi8g/zh-cn_image_0000002779405144.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=69914D06311D6EB9DD9C5DB41F38F7E91E2CC5B041AE0F3935D08074A6D23CE9)，或者点击模拟器工具栏上的关闭按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/s641ytMQRZmpvR4jN4ywhQ/zh-cn_image_0000002779405130.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=E7250ED3BD0E4FEE78E2E127513E99E1903A74BCC6C7AD46594426183B858846)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/8KX68wDITfKTlMElSklQ0Q/zh-cn_image_0000002808884733.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=D2795522C8A8F333EA07B69BB13FBDCABF0DCF170B8EC0A91C6E37104C743A30 "点击放大")

模拟器关闭后，点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/xzJjr9D7T3eQTvl7533oqg/zh-cn_image_0000002779405126.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=2D47B60F5750AA1AB95350AAA59D263F40FDBBB7109117FFD885DA4C56D68110) **> Delete**可以删除模拟器，并清除模拟器的用户数据和配置信息。
