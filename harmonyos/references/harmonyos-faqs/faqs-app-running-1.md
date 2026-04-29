---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-1
title: 登录华为开发者账号后，提示需要实名认证
breadcrumb: FAQ > DevEco Studio > 应用运行 > 登录华为开发者账号后，提示需要实名认证
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:11+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:086cc71b5564412a9d6131d2198293a1db3751f55fac427314485f98b0ccc7ec
---

**问题现象**

使用本地模拟器时，需用实名认证的开发者账号登录授权。若账号未实名认证，本地模拟器会提示需要实名认证。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/gDC2rd-4To-9R0R0YwOFlw/zh-cn_image_0000002194158868.png?HW-CC-KV=V1&HW-CC-Date=20260429T062111Z&HW-CC-Expire=86400&HW-CC-Sign=3BAAABD0020DCC8B4659E240A5F6088B9260A1DBAE12A8D77467B08614552F6D "点击放大")

**解决措施**

原因包括以下两种情况：

* 华为账号未实名认证，请开发者按照如下步骤进行处理。
* 刚完成实名认证但认证未生效，开发者可根据步骤4清除浏览器Cookie后重试。

1. 点击上图中的**Verify Identity**，前往开发者联盟实名认证。
2. 根据浏览器界面提示进行实名认证，具体指导可以参考[实名认证介绍](../start/itrna-0000001076878172.md)。个人开发者可以选择银行卡认证或者身份证认证。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/vKC3U1cpTPu_M6RTUkpXIg/zh-cn_image_0000002194318476.png?HW-CC-KV=V1&HW-CC-Date=20260429T062111Z&HW-CC-Expire=86400&HW-CC-Sign=91F536BB9F7A5AD8C35E0C30370B6BB77B7109D38B4A403F05C5DB48D8062D30 "点击放大")
3. 认证完成后，在DevEco Studio界面，点击右上角个人中心，点击Sign out退出，重新登录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/7b4xHLbcSsSD1qmwJqCibA/zh-cn_image_0000002194318480.png?HW-CC-KV=V1&HW-CC-Date=20260429T062111Z&HW-CC-Expire=86400&HW-CC-Sign=9B4C9E84E0A427E70CACC7F7905946BA7089843475C34C3C6678F471FE076ED5)
4. （可选）如果实名认证后重新登录，仍提示需要进行实名认证，可清除浏览器 **Cookie（快捷键 Ctrl+Shift+Del）**后重试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/Dk8LPAmRR42o9Qj8ACagUQ/zh-cn_image_0000002229604249.png?HW-CC-KV=V1&HW-CC-Date=20260429T062111Z&HW-CC-Expire=86400&HW-CC-Sign=0A4B370F38535002A9374551020D902D98AF98B1BF79E4F679D38F874825D20B "点击放大")
