---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-faq-23
title: 自动续期订阅商品，A切换B且立即生效时，新订阅有效期的组成
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > IAP Kit常见问题 > 自动续期订阅商品，A切换B且立即生效时，新订阅有效期的组成
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e8efdc550a048e52ba875ab06edafbd93fcd0be70bd987f78e1c6a8335166a6a
---

订阅在发生切换且立即生效时，原订阅的剩余权益价值会自动按照比例，折算并叠加至新订阅。所以，切换后订阅有效期的组成 = 原订阅剩余权益的折算时间 + 新订阅原本的周期时间。

比如，某个用户首先购买了订阅A（普通会员，20元/30天），使用了15天后，切换成同订阅组下的订阅B（高级会员，60元/30天）。切换时，A订阅剩余权益自动按比例折算，折算至B订阅的时间为5天。则切换后，B订阅有效期的天数 = 5天 + 30天 = 35天。

时间轴（MM/dd）如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/kuLWVKZ1RhikBn2rWuRLYw/zh-cn_image_0000002788308078.png?HW-CC-KV=V1&HW-CC-Date=20261114T004822Z&HW-CC-Expire=31536000000&HW-CC-Sign=BA995F72851DE3BD9ACF68BB310DE23769BB8510545CC3BB3A4E229AAB3D97FA)

对于沙盒环境，按照生产1天 = 沙盒10s换算，等效时间轴（hh:mm:ss）如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/1QDcrHfuR5Sk3RlMKn0RCQ/zh-cn_image_0000002817427441.png?HW-CC-KV=V1&HW-CC-Date=20261114T004822Z&HW-CC-Expire=31536000000&HW-CC-Sign=B0DD2A2FE8451C601A1DE4F492F98D45DBBFF986B0C34896FAB274514F011C0A)
