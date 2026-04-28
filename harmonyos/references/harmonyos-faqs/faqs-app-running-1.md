---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-1
title: 登录华为开发者账号后，提示需要实名认证
breadcrumb: FAQ > DevEco Studio > 应用运行 > 登录华为开发者账号后，提示需要实名认证
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:56+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:4db8dee136d99a34eb2eeeb2cc69566ebd87dabd771ef598242eb574e8eed05d
---

**问题现象**

使用本地模拟器时，需用实名认证的开发者账号登录授权。若账号未实名认证，本地模拟器会提示需要实名认证。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/gDC2rd-4To-9R0R0YwOFlw/zh-cn_image_0000002194158868.png?HW-CC-KV=V1&HW-CC-Date=20260428T002954Z&HW-CC-Expire=86400&HW-CC-Sign=AB6CC44512161B16E02DE543C713C34FC78473BA793AF558570F2B0020545AB4 "点击放大")

**解决措施**

原因包括以下两种情况：

* 华为账号未实名认证，请开发者按照如下步骤进行处理。
* 刚完成实名认证但认证未生效，开发者可根据步骤4清除浏览器Cookie后重试。

1. 点击上图中的**Verify Identity**，前往开发者联盟实名认证。
2. 根据浏览器界面提示进行实名认证，具体指导可以参考[实名认证介绍](../start/itrna-0000001076878172.md)。个人开发者可以选择银行卡认证或者身份证认证。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/vKC3U1cpTPu_M6RTUkpXIg/zh-cn_image_0000002194318476.png?HW-CC-KV=V1&HW-CC-Date=20260428T002954Z&HW-CC-Expire=86400&HW-CC-Sign=85A8E7894A4F7537A53F6A713E183F627015492857232EE4CDA2942C7A7A3C68 "点击放大")
3. 认证完成后，在DevEco Studio界面，点击右上角个人中心，点击Sign out退出，重新登录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/7b4xHLbcSsSD1qmwJqCibA/zh-cn_image_0000002194318480.png?HW-CC-KV=V1&HW-CC-Date=20260428T002954Z&HW-CC-Expire=86400&HW-CC-Sign=BBD23DF55FF5893B349B60851B687E5194D347D6F4715F5E0126A1FA509F873D)
4. （可选）如果实名认证后重新登录，仍提示需要进行实名认证，可清除浏览器 **Cookie（快捷键 Ctrl+Shift+Del）**后重试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/Dk8LPAmRR42o9Qj8ACagUQ/zh-cn_image_0000002229604249.png?HW-CC-KV=V1&HW-CC-Date=20260428T002954Z&HW-CC-Expire=86400&HW-CC-Sign=D4F67C1BC1811256684B1CF02249624ECB22E1C7D67A18737CA4E180A05C5202 "点击放大")
