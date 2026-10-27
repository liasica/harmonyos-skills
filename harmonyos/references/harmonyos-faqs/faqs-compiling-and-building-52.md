---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-52
title: 如何给新增的module在线签名
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何给新增的module在线签名
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:53+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:c2c448b9cc2040f57fcd098339d18df09d48f58428ab6e9a67ee577070af9735
---

操作步骤：

1. 连接真机设备，确保[DevEco Studio与真机设备已连接](../harmonyos-guides/ide-run-device.md)，真机连接成功后如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/yJ10JwWjStWG341rJmwAIA/zh-cn_image_0000002624478514.png)
2. 进入 File > Project Structure... > Project > Signing Configs 界面，勾选“Automatically generate signature”。如果是 HarmonyOS 工程，还需勾选“Support HarmonyOS”。若未登录，请先单击 Sign In 进行登录，然后完成签名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/uGT_TlI8SIKJobdg6cqcgw/zh-cn_image_0000002654797873.png "点击放大")

   签名完成后，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/_aoT9RMAQ3itQ4k49iROQA/zh-cn_image_0000002624638418.png "点击放大")
