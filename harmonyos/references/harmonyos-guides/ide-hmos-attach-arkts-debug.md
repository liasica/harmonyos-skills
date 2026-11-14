---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-attach-arkts-debug
title: attach启动调试
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > attach启动调试
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:16+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:1dfdbc89d55c6be611b138503db389e7f5ed3edae05668e17c27fc4e9b1e3acb
---

开发者也可以通过将调试程序附加到已运行的应用进行调试。

附加调试和调试的区别在于，附加调试可以先运行应用/元服务，然后再启动调试，或者直接启动设备上已安装的应用/元服务进行调试；而调试是直接运行应用/元服务后立即启动调试。

## 前提条件

当前设备上被附加调试的应用代码和本地代码一致，且已提前进行构建生成必要的sourceMap文件。

## 使用约束

附加调试不支持的场景：

* 本地无源码。
* 应用包名不匹配，将出现提示“**所选进程与当前项目的包名不匹配！**”，但不阻塞调试过程。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/BSKwrOMmT-CFXSibAx5Hzw/zh-cn_image_0000002781311070.png?HW-CC-KV=V1&HW-CC-Date=20261114T004727Z&HW-CC-Expire=31536000000&HW-CC-Sign=9B268E2D20FD15EFDC6E5E0E741491B1801A430833DF9B865BBBD9FCCCD7475F)

## 操作步骤

1. 在工具栏中，选择调试的设备，并单击附加调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/GHNFD_Z-TxqqJ-nODw1lAg/zh-cn_image_0000002810750669.png?HW-CC-KV=V1&HW-CC-Date=20261114T004727Z&HW-CC-Expire=31536000000&HW-CC-Sign=4CB86A84A769E6D1C7EEAC2FB76384DE15AA16B5B9C477CF31F13DCF711295BD)
2. 选择要调试的应用进程，若应用包名与当前工程不一致，则需勾选**显示所有进程**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/soAxWw_FTbWvIF34JEkYpA/zh-cn_image_0000002810750685.png?HW-CC-KV=V1&HW-CC-Date=20261114T004727Z&HW-CC-Expire=31536000000&HW-CC-Sign=CE36169739671D390F4E673D1E19D23A4ACB4C5D36D80BF16F17964FC7F3B357)
3. 选择需要使用的调试配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/N5eg5DmlTXm5LPCdvd9-cQ/zh-cn_image_0000002781471006.png?HW-CC-KV=V1&HW-CC-Date=20261114T004727Z&HW-CC-Expire=31536000000&HW-CC-Sign=A2857F56E423562159B759579093290601477B9D19116FE28BB12865BA5D81BA)
4. 选择好调试配置进行附加调试后，**调试类型**不可改变，只可在**运行/调试配置**界面修改。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/LAp7TRxGRsiaQhCcofDieA/zh-cn_image_0000002781311076.png?HW-CC-KV=V1&HW-CC-Date=20261114T004727Z&HW-CC-Expire=31536000000&HW-CC-Sign=993039E7A71496325037A7DC596345EEBA11D82AD205856F0470B7161EE1409A)
5. 点击**确定**开始附加调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/_DnjVbDmSmaOF0TbcEmGzw/zh-cn_image_0000002810630559.png?HW-CC-KV=V1&HW-CC-Date=20261114T004727Z&HW-CC-Expire=31536000000&HW-CC-Sign=31F46084975AF626B76A63904E0D4B715791BA61C918A71455433503E45FF238)
