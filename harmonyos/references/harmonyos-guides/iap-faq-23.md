---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-faq-23
title: 自动续期订阅商品，A切换B且立即生效时，新订阅有效期的组成
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > IAP Kit常见问题 > 自动续期订阅商品，A切换B且立即生效时，新订阅有效期的组成
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fcd476f4262cbd4cb0f9c6dd9ff65511dec32aaa4bc362b1823f3df37ccf1695
---

订阅在发生切换且立即生效时，原订阅的剩余权益价值会自动按照比例，折算并叠加至新订阅。所以，切换后订阅有效期的组成 = 原订阅剩余权益的折算时间 + 新订阅原本的周期时间。

比如，某个用户首先购买了订阅A（普通会员，20元/30天），使用了15天后，切换成同订阅组下的订阅B（高级会员，60元/30天）。切换时，A订阅剩余权益自动按比例折算，折算至B订阅的时间为5天。则切换后，B订阅有效期的天数 = 5天 + 30天 = 35天。

时间轴（MM/dd）如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/FHMwZ6xFSae2sUzoNflJ8A/zh-cn_image_0000002786520274.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=54BBE83E3353733219338264FFC49C404714CEE1DB8D4C17064A3EEB36BAE9F1)

对于沙盒环境，按照生产1天 = 沙盒10s换算，等效时间轴（hh:mm:ss）如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/n82_fWMFRLWXq_CtPF8oHw/zh-cn_image_0000002786360346.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=B002CA4B9DD8A18616CC130FD71942B76532BBBE204D7EC2064780DFB74BA4C1)
