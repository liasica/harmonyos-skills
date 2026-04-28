---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-faq-21
title: 请求接口加签验证中，如果请求头“PayMercAuth”中bodySign字段为空值，会做验签吗？还是会先校验字段？
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > Payment Kit常见问题 > 请求接口加签验证中，如果请求头“PayMercAuth”中bodySign字段为空值，会做验签吗？还是会先校验字段？
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:18+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:da0954b713523ac43cdd3d72d237f788ae890b7460e57ef39adedaaad40384e1
---

鉴权请求头“PayMercAuth”会先校验相关字段再做验签。bodySign字段设置为空值，Payment Kit服务器不会做验签，直接响应异常给商户。
