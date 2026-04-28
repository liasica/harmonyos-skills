---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-52
title: 如何给新增的module在线签名
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何给新增的module在线签名
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:18+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:da713206120b22df9fe3b60e22a1beb0bb5176b1401f8ccc9abef4d4edf4ef1f
---

操作步骤：

1. 连接真机设备，确保[DevEco Studio与真机设备已连接](../harmonyos-guides/ide-run-device.md)，真机连接成功后如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/fcwr7Oi4TVu3ZzY_-2YEvA/zh-cn_image_0000002229604037.png?HW-CC-KV=V1&HW-CC-Date=20260428T002917Z&HW-CC-Expire=86400&HW-CC-Sign=B27AD528577094AF6DB39A8AEECB5D5B12739BAF534A05374F2411A9D59FB627)
2. 进入 File > Project Structure... > Project > Signing Configs 界面，勾选“Automatically generate signature”。如果是 HarmonyOS 工程，还需勾选“Support HarmonyOS”。若未登录，请先单击 Sign In 进行登录，然后完成签名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/LKyP5QQ7QFSWnwVGNEzCwQ/zh-cn_image_0000002229758513.png?HW-CC-KV=V1&HW-CC-Date=20260428T002917Z&HW-CC-Expire=86400&HW-CC-Sign=695C6EC030760CF5CEE37CFF7A159DCE4A63624E430FC84398FDB98040FBAA69 "点击放大")

   签名完成后，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/vDXljEbjS2m9rmrRPxOaPw/zh-cn_image_0000002194318264.png?HW-CC-KV=V1&HW-CC-Date=20260428T002917Z&HW-CC-Expire=86400&HW-CC-Sign=F85E4D889924DBB4F0DAAB2478315A59BC998E48EDE94EBECB7D9E4B434E73A6 "点击放大")
