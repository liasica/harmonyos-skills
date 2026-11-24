---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-start-and-close
title: 启动和关闭模拟器
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 使用模拟器运行应用 > 管理模拟器 > 启动和关闭模拟器
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:29+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:ecb6f4f32db1f5e204667c0e044e2808a32437fc26c4f7197111742a9c05e61f
---

在设备管理器页面，单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/612fl6XzSzavsPH7WwyUaA/zh-cn_image_0000002779405122.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=E24E8DD4622A4F0789CCB15785765F7C1893D692C8384FC57FB04F24FF579B56)即可启动模拟器。模拟器启动时会默认携带之前运行时的用户数据，包括用户上传的文件，安装的应用等。如果是新创建的模拟器，则不会携带用户数据。如果想清除之前运行时的用户数据，点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/S0CiNFYMSeOW9UCPNStNmA/zh-cn_image_0000002808764673.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=814726F9B71B1C40342CFBBE4EAF3E569286393C0FB66898F7F2E34A4106D74A) **> Wipe User Data**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/g9dBAhftQK2f7obvPrc0XA/zh-cn_image_0000002779565078.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=7795DDE94DE7DB1A9BB5413BF18E63257EDCBDE39ED5A71640955010C8A4F17E "点击放大")

从DevEco Studio 6.1.0 Beta1版本开始，如果创建模拟器时选择热启动，则启动模拟器时会加载上次关闭时保存的快照，启动后会恢复至上次关闭时的状态。热启动后，多屏状态会恢复为单屏状态。

从26.0.0版本开始，如果热启动后出现异常，可点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/Y9Qf2XYNSRSSnREWvZMjsg/zh-cn_image_0000002779405132.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=DE345FA5454BA73E5AFB01627DF1F5D50AB87F5E435530620E6795922EB1F09D) **> Cold Boot**，本次将以冷启动方式启动模拟器，并且会保留之前的用户数据，关闭模拟器时仍会保存快照。

例如推包运行后关闭模拟器，再次启动时会显示在上次运行的界面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/mOHpDTFoRt-AOQUjwC8TeQ/zh-cn_image_0000002808884783.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=C7FA5922DA0EBCAFDBB6685A6C847704C68E946B6CB21B2E0B9E5333054E9CAF "点击放大")

在模拟器运行期间，可以点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/MxPRHJNjQDOhQ6HS5pdxdw/zh-cn_image_0000002779565086.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=5AFFE6E2C2F982E5B4A12D56A1C1902D2397433E2EB00B819102BC1639F1D235) **> Show on Disk**显示模拟器在本地生成的用户数据。点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/vo3D-fCjR3Gh7woSjpb3fA/zh-cn_image_0000002808764655.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=2F8F7E357E57E559A28D866BEDFB6EF9BCFDD72223DB81990121279FEE6F69D1) **> Generate logs**可以生成模拟器自启动到此刻的所有日志信息。想要关闭运行中的模拟器，可以在设备管理器页面点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/xRXnEZTJSHmvm94EUsJODQ/zh-cn_image_0000002779405144.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=E98D1F8D6DA61C249D957D8C71763EC76ACF6A4A0C57D9BEC0EDE59A51429A0D)，或者点击模拟器工具栏上的关闭按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/5VYOE1PrREm9xMvf6FyMDg/zh-cn_image_0000002779405130.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=3538F34A4A2C196A52FB0AD5134B67EA5FCA96B60B5A995848A9816CD902F286)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/9oXou6DORv2NI4LU0cbLHw/zh-cn_image_0000002808884733.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=7F94B5DFC1A54B58D7CCEEE9651A1EAF5C36C6239087723ACDD9054E4ED6EFDE "点击放大")

模拟器关闭后，点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/182dbMZQQC-4vMjhlpvtYA/zh-cn_image_0000002779405126.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=A389E0460A73AA3114610B5A03B1FFA5E3AD43F98D2A8444790F568BDDEFD95C) **> Delete**可以删除模拟器，并清除模拟器的用户数据和配置信息。
