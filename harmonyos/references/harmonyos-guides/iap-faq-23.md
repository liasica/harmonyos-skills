---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-faq-23
title: 自动续期订阅商品，A切换B且立即生效时，新订阅有效期的组成
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > IAP Kit常见问题 > 自动续期订阅商品，A切换B且立即生效时，新订阅有效期的组成
category: harmonyos-guides
scraped_at: 2026-04-29T13:38:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ccb0f5bd91d1b4e4f1c17beb40268621b14e645348d1fc5c976ce8e9fcc421df
---

订阅在发生切换且立即生效时，原订阅的剩余权益价值会自动按照比例，折算并叠加至新订阅。所以，切换后订阅有效期的组成 = 原订阅剩余权益的折算时间 + 新订阅原本的周期时间。

比如，某个用户首先购买了订阅A（普通会员，20元/30天），使用了15天后，切换成同订阅组下的订阅B（高级会员，60元/30天）。切换时，A订阅剩余权益自动按比例折算，折算至B订阅的时间为5天。则切换后，B订阅有效期的天数 = 5天 + 30天 = 35天。

时间轴（MM/dd）如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/ZPxeLJZJTyC3mQOjE5Duqw/zh-cn_image_0000002558765448.png?HW-CC-KV=V1&HW-CC-Date=20260429T053845Z&HW-CC-Expire=86400&HW-CC-Sign=7F13D6763F6BA76334D8EABA06AB507583C33DCBF92A1E6E0130FBD5A4EF5F43)

对于沙盒环境，按照生产1天 = 沙盒10s换算，等效时间轴（hh:mm:ss）如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/4BzHtv2fS_-PrF43agkZWA/zh-cn_image_0000002558605792.png?HW-CC-KV=V1&HW-CC-Date=20260429T053845Z&HW-CC-Expire=86400&HW-CC-Sign=9EDFDE0B2A895AC859ACE7672D3FC056C58F6A1EA1A980CF39ABB18DF291508C)
