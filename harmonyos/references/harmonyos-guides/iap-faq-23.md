---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-faq-23
title: 自动续期订阅商品，A切换B且立即生效时，新订阅有效期的组成
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > IAP Kit常见问题 > 自动续期订阅商品，A切换B且立即生效时，新订阅有效期的组成
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c6c868bb25a0e1229781cea3268c84b36263d7d6d633f3c390da74881350da64
---

订阅在发生切换且立即生效时，原订阅的剩余权益价值会自动按照比例，折算并叠加至新订阅。所以，切换后订阅有效期的组成 = 原订阅剩余权益的折算时间 + 新订阅原本的周期时间。

比如，某个用户首先购买了订阅A（普通会员，20元/30天），使用了15天后，切换成同订阅组下的订阅B（高级会员，60元/30天）。切换时，A订阅剩余权益自动按比例折算，折算至B订阅的时间为5天。则切换后，B订阅有效期的天数 = 5天 + 30天 = 35天。

时间轴（MM/dd）如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/N9m7WmwHRuCxFMjPumom7A/zh-cn_image_0000002552958948.png?HW-CC-KV=V1&HW-CC-Date=20260427T234933Z&HW-CC-Expire=86400&HW-CC-Sign=F059E81CDB80488AAB3A4787B803117B8F613B3305C2AAB0D6A07A7DA3CAC688)

对于沙盒环境，按照生产1天 = 沙盒10s换算，等效时间轴（hh:mm:ss）如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/_BBRZSbxQRmYJRCY7RWP4A/zh-cn_image_0000002583478949.png?HW-CC-KV=V1&HW-CC-Date=20260427T234933Z&HW-CC-Expire=86400&HW-CC-Sign=80371787B6CC04E427F9D10999837549238209FA0540FAC81AC328ABE817E815)
