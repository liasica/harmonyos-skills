---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-faq-23
title: 自动续期订阅商品，A切换B且立即生效时，新订阅有效期的组成
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > IAP Kit常见问题 > 自动续期订阅商品，A切换B且立即生效时，新订阅有效期的组成
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:35d90c8588dbde1ee9cc76c025584ff2d4c9e30f4dad8abc2fba4021b6d39a50
---

订阅在发生切换且立即生效时，原订阅的剩余权益价值会自动按照比例，折算并叠加至新订阅。所以，切换后订阅有效期的组成 = 原订阅剩余权益的折算时间 + 新订阅原本的周期时间。

比如，某个用户首先购买了订阅A（普通会员，20元/30天），使用了15天后，切换成同订阅组下的订阅B（高级会员，60元/30天）。切换时，A订阅剩余权益自动按比例折算，折算至B订阅的时间为5天。则切换后，B订阅有效期的天数 = 5天 + 30天 = 35天。

时间轴（MM/dd）如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/nClJ8LtlTBuv9_VbKC8cBQ/zh-cn_image_0000002792878060.png?HW-CC-KV=V1&HW-CC-Date=20261121T011229Z&HW-CC-Expire=31536000000&HW-CC-Sign=F19A2BF634E4C3E0EFFCBE4B734C56E39ED7B2F70B1B928A65EF5A6F906C0F10)

对于沙盒环境，按照生产1天 = 沙盒10s换算，等效时间轴（hh:mm:ss）如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/Wed4xreRSaaZvaU5TvoRYw/zh-cn_image_0000002821837967.png?HW-CC-KV=V1&HW-CC-Date=20261121T011229Z&HW-CC-Expire=31536000000&HW-CC-Sign=0FDBE37E74A7583246BF17A48408A2FDC6D29E928823580F5293A59F0F39E7E7)
