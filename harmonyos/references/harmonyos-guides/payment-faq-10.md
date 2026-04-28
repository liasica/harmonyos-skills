---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-faq-10
title: 接口请求响应“无效的签名”应该如何排查？
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > Payment Kit常见问题 > 接口请求响应“无效的签名”应该如何排查？
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:306ee4c8af69e3b3fea37db0fa80c3783c44ce51f7e9de43920bfe67b9a8ed20
---

1. 加签私钥和上传到商户平台的公钥是否配对。
2. 排查待加签字符串是否正确拼接。 对象内的待加签字段需要排序后再拼接。对象内的嵌套的下一级对象也需要排序后再拼接。具体示例参考[签名规则](../harmonyos-references/payment-rest-overview.md#签名规则)。
3. 排序拼接的字段命名和请求参数命名方式是否一致（如加签字段使用了匈牙利命名方式，请求参数则用小驼峰命名方式，导致加签验证内容不一致）。
4. 相关加签内容字段（如sign）内容是否正确设置（如加签后内容未及时设置到sign字段，一直使用固定的sign内容去发起请求）。
5. 检查加签算法是否和要求的加签算法一致。
