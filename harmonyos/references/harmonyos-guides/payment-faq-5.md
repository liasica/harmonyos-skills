---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-faq-5
title: 拉起收银台无反应或报错？
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > Payment Kit常见问题 > 拉起收银台无反应或报错？
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2f99ca67bbf93306b080f390235fc89a9db11d3732f21449b32a1d3b3e0c499f
---

该情况一般属于入参格式存在问题，还请根据支付的回调信息进行定位，请检查以下注意事项：

* 检查[orderStr](../harmonyos-references/payment-model.md#orderstr)入参格式，要求为JsonStr的格式（参见[示例代码](payment-payment-process.md#拉起华为支付收银台端侧开发)），不可为json对象或重复序列化。
* 请确保每次的支付请求noncestr参数唯一。
* 请检查timestamp时间戳格式是否错误。
* 请检查签名前是否已排序拼接。
* 签名后的入参字段重新赋值。
* 对应prepay\_id的订单是否已过期或已支付。
