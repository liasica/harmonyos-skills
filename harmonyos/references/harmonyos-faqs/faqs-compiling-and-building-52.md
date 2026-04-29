---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-52
title: 如何给新增的module在线签名
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何给新增的module在线签名
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:31+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ffa9f6b8dce461df400e30cdf065c25d867fafd77bd0794dc6add879a42dadfe
---

操作步骤：

1. 连接真机设备，确保[DevEco Studio与真机设备已连接](../harmonyos-guides/ide-run-device.md)，真机连接成功后如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/fcwr7Oi4TVu3ZzY_-2YEvA/zh-cn_image_0000002229604037.png?HW-CC-KV=V1&HW-CC-Date=20260429T062030Z&HW-CC-Expire=86400&HW-CC-Sign=BEAF2A4D974BD0A3732FE6CC2522E2B1FF43CB1593C92CB73607AB4B8027A9A3)
2. 进入 File > Project Structure... > Project > Signing Configs 界面，勾选“Automatically generate signature”。如果是 HarmonyOS 工程，还需勾选“Support HarmonyOS”。若未登录，请先单击 Sign In 进行登录，然后完成签名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/LKyP5QQ7QFSWnwVGNEzCwQ/zh-cn_image_0000002229758513.png?HW-CC-KV=V1&HW-CC-Date=20260429T062030Z&HW-CC-Expire=86400&HW-CC-Sign=1C92CD2740DBEE1D34636B13864C98A4D1BFAF36DEEB8B2A1E9242D7DBBEA418 "点击放大")

   签名完成后，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/vDXljEbjS2m9rmrRPxOaPw/zh-cn_image_0000002194318264.png?HW-CC-KV=V1&HW-CC-Date=20260429T062030Z&HW-CC-Expire=86400&HW-CC-Sign=2AF2392F030A2D8CB9428260D17070BB242A9BD9620A4783355D7E6D8C50B868 "点击放大")
