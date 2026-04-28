---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-start-and-close
title: 启动和关闭模拟器
breadcrumb: 指南 > 编写与调试应用 > 使用模拟器运行应用 > 管理模拟器 > 启动和关闭模拟器
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3a8d399975451ea99ea3564f09b97ecff5a66234a9dbb6c1885b5d803c375bfe
---

在设备管理器页面，单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/aSnvN2DxSw-HlLzUlyEkug/zh-cn_image_0000002530911082.png?HW-CC-KV=V1&HW-CC-Date=20260427T235641Z&HW-CC-Expire=86400&HW-CC-Sign=1E6440DA3C374B195A4B43E2395B4CCEF8C32FA862C72C5B18FFCCE9AFE2BDEE)即可启动模拟器。模拟器启动时会默认携带之前运行时的用户数据，包括用户上传的文件，安装的应用等。如果是新创建的模拟器，则不会携带用户数据。如果想清除之前运行时的用户数据，点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/zkw7qaW0TymlHUm1s6Wdiw/zh-cn_image_0000002561831005.png?HW-CC-KV=V1&HW-CC-Date=20260427T235641Z&HW-CC-Expire=86400&HW-CC-Sign=274E4FE24E714EE914D80E8931E210EA3E45E736441C1986C6B2EE2CE7A2EAB2) **> Wipe User Data**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/JbarmuRATnSpBWYQldZ4Xg/zh-cn_image_0000002530751076.png?HW-CC-KV=V1&HW-CC-Date=20260427T235641Z&HW-CC-Expire=86400&HW-CC-Sign=C35EEC3DD4A64782BDAA2CC81655F37C2EF6461A8323A1AFE74FB9FF06605202 "点击放大")

从DevEco Studio 6.1.0 Beta1版本开始，如果创建模拟器时选择热启动，则启动模拟器时会加载上次关闭时保存的快照，启动后会恢复至上次关闭时的状态。热启动后，多屏状态会恢复为单屏状态，折叠屏模拟器会恢复成默认展开状态。

如果热启动后出现异常，可点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/w8OrzaBtQfint22GYB-VUQ/zh-cn_image_0000002561751033.png?HW-CC-KV=V1&HW-CC-Date=20260427T235641Z&HW-CC-Expire=86400&HW-CC-Sign=07851138329E8BA41ED9610642EF2C7E64B8706E1C3837EB2324657C9135A6F3) **> Wipe User Data**清除用户数据后重新启动。

例如推包运行后关闭模拟器，再次启动时会显示在上次运行的界面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/1wmOMvE8ToyEs74Q-cylgA/zh-cn_image_0000002530911092.png?HW-CC-KV=V1&HW-CC-Date=20260427T235641Z&HW-CC-Expire=86400&HW-CC-Sign=F632BB27B4A28EC94365D74DE402016A5535483AE1E2CCEA3E6160C4CB9797A7 "点击放大")

在模拟器运行期间，可以点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/VYiOyv-4TY6xo0-TVm49zQ/zh-cn_image_0000002561751025.png?HW-CC-KV=V1&HW-CC-Date=20260427T235641Z&HW-CC-Expire=86400&HW-CC-Sign=3D1FD12190E1E7266B3EBFC91C50D413D81C64E850E4D14E53C225605845857D) **> Show on Disk**显示模拟器在本地生成的用户数据。点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/VpRdbrHASzyOnpQYJhme3g/zh-cn_image_0000002561751021.png?HW-CC-KV=V1&HW-CC-Date=20260427T235641Z&HW-CC-Expire=86400&HW-CC-Sign=753E8553C8DA2D757FBECCEEB97251AFDCB4BD54C754B6403553471527DC5468) **> Generate logs**可以生成模拟器自启动到此刻的所有日志信息。想要关闭运行中的模拟器，可以在设备管理器页面点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/2PPN75xMSHGy-hnPlKAiYQ/zh-cn_image_0000002530751080.png?HW-CC-KV=V1&HW-CC-Date=20260427T235641Z&HW-CC-Expire=86400&HW-CC-Sign=3DD8666B0F588198BE9C986136B7CBF71648808174C932102E7566053EC47C77)，或者点击模拟器工具栏上的关闭按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/mZqA0Z5bTSWoUZ8QIevh_Q/zh-cn_image_0000002530751090.png?HW-CC-KV=V1&HW-CC-Date=20260427T235641Z&HW-CC-Expire=86400&HW-CC-Sign=F595F445DF790534A54CFCBA81AE5754F9D5160B9BAA728298756832A6B04EA5)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/qdkl8LrAR_-b_8VQrmdBpA/zh-cn_image_0000002561751013.png?HW-CC-KV=V1&HW-CC-Date=20260427T235641Z&HW-CC-Expire=86400&HW-CC-Sign=791F9F2BBFE7FCEA0BD011CBE4DB9C7D4BF1E56B56E17683A88F1C7E7FB6FCDE "点击放大")

模拟器关闭后，点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/1UpqVERUQQitUcwlvt0MTQ/zh-cn_image_0000002530911084.png?HW-CC-KV=V1&HW-CC-Date=20260427T235641Z&HW-CC-Expire=86400&HW-CC-Sign=A3CAC63ABA0C10ED134D5EEED04DBDC0B6FB40BA6FEF94FAC78BF6A5B4122367) **> Delete**可以删除模拟器，并清除模拟器的用户数据和配置信息。
