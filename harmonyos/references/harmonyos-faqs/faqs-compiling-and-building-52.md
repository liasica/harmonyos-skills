---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-52
title: 如何给新增的module在线签名
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何给新增的module在线签名
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:31+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:6a526b126382d2028d22925a10a5aa61024b02e5e63395bc1d0c642ae7f87125
---

操作步骤：

1. 连接真机设备，确保[DevEco Studio与真机设备已连接](../harmonyos-guides/ide-run-device.md)，真机连接成功后如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/fcwr7Oi4TVu3ZzY_-2YEvA/zh-cn_image_0000002229604037.png)
2. 进入 File > Project Structure... > Project > Signing Configs 界面，勾选“Automatically generate signature”。如果是 HarmonyOS 工程，还需勾选“Support HarmonyOS”。若未登录，请先单击 Sign In 进行登录，然后完成签名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/LKyP5QQ7QFSWnwVGNEzCwQ/zh-cn_image_0000002229758513.png "点击放大")

   签名完成后，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/vDXljEbjS2m9rmrRPxOaPw/zh-cn_image_0000002194318264.png "点击放大")
