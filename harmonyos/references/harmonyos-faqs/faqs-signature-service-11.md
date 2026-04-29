---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-11
title: 签名时，提示“Failed to query agreement signing records”
breadcrumb: FAQ > DevEco Studio > 签名服务 > 签名时，提示“Failed to query agreement signing records”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:09+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:86d25d0ed28c1f371c74ad911acd6a45579bcf188c29c743131c09478c706f40
---

**问题现象**

使用未实名认证的华为账号登录会导致签名错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/VGs7leiwRY6JGc9E9Ni7Sg/zh-cn_image_0000002194318468.png?HW-CC-KV=V1&HW-CC-Date=20260429T062109Z&HW-CC-Expire=86400&HW-CC-Sign=9C05BE3C611B003E51C4472AEA9C9757519D0049475E0A6F73DA29EA45264FEC)

**解决措施**

出现该问题的原因是签名过程中，DevEco Studio与查询协议的连接通道发生异常

请尝试以下两种方法解决此问题

方式一：该问题可能是由于DevEco Studio的HTTP代理问题引起的，请参考[配置代理](../harmonyos-guides/ide-environment-config.md)。

方式二：进行开发者实名认证，具体指导可以参考[实名认证介绍](../start/itrna-0000001076878172.md)。
